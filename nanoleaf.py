import http.client as httplib
import json
import socket
from dataclasses import dataclass
from enum import Enum

import data
import utils


class Color(Enum):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    ORANGE = (255, 127, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)


@dataclass
class PanelUpdate:
    row: int
    col: int
    color: str
    transition_time: int = 0.5


@dataclass
class Position:
    row: int
    col: int
    controller_id: int
    panel_id: int


@dataclass
class PhysicalPosition:
    panelId: int
    x: int
    y: int
    o: int  # 0, 180, or 360


@dataclass
class Frame:
    panel_id: int
    red: int
    green: int
    blue: int
    transition_time: int


class Nanoleaf:
    _API_PORT = 16021
    _API_BASE = "api/v1"
    _SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    _SOCK_PORT = 60221
    IPS = [
        "192.168.1.14",
        "192.168.1.13",
        "192.168.1.12",
        "192.168.1.10",
        "192.168.1.11",
        "192.168.1.9",
        "192.168.1.4",
        "192.168.1.5",
        "192.168.1.3",
        "192.168.1.2",
    ]
    AUTH_CODES = [
        "4xjvV9IJAQDq83SFaROVVzvble3vHwV8",
        "LlBI3Odz7EOHR3v5TPwh4fDbGrFuKSq7",
        "WKiepsgP7vhnfI4zGBmxVH26Rq6KNFgg",
        "28vOnfDhQZXeShXjGKWocxHZJUe9NCwn",
        "vioLVKiV1IgfsAA94JFFBTFy0vEUG48K",
        "UY3DEDumg19xCnwrNV4Btm2FPF0CAhdO",
        "0AJgQMml89aa12iAYpAqEoWKrKW18JZa",
        "5EpekYkcVupgIjXM37bRsNG0pE38NfGC",
        "cSTCTsuAgBRC7i8F3ug1cc1Z1smDyPQH",
        "kAbYywuZWBWsMrFsOluxbnqAXEQqyMKr",
    ]

    def __init__(self, demo_mode: bool = False):
        if demo_mode:
            panels = self._initialize_controller(self.IPS[7], self.AUTH_CODES[7])
            self._panel_position_map: dict[tuple[int, int], Position] = {}
            for j, panel in enumerate(panels):
                row, col = data.panel_positions[7][j]
                self._panel_position_map[(row, col)] = Position(
                    row=row,
                    col=col,
                    controller_id= 7,
                    panel_id=panel["panelId"],
                )
        else:
            controller_data = [
                self._initialize_controller(ip, auth) for ip, auth in zip(self.IPS, self.AUTH_CODES)
            ]
            self._map_panel_positions(controller_data)

    def _request(self, mode: str, ip: str, auth: str, endpoint: str, data: dict = None):
        LISTENER = ip + ":" + str(self._API_PORT)
        try:
            conn = httplib.HTTPConnection(LISTENER)
            if data is not None:
                conn.request(
                    mode,
                    "/api/v1/" + auth + "/" + endpoint,
                    json.dumps(data),
                    {"Content-Type": "application/json"},
                )
            else:
                conn.request(mode, "/api/v1/" + auth + "/" + endpoint)
            response = conn.getresponse()
            body = response.read()
            if len(body) != 0:
                body = json.loads(body)
            return body

        except (httplib.HTTPException, socket.error) as ex:
            print(f"Error: {ex}")

    def _format_api_url(self, ip: str, auth: str, endpoint: str) -> str:
        return f"https://{ip}:{self._API_PORT}/{self._API_BASE}/{auth}/{endpoint}"

    def _initialize_controller(self, ip: str, auth: str) -> list[PhysicalPosition]:
        """
        Initializes the controller and returns the position data.
        """
        self._set_stream_control_mode(ip, auth)
        return self._get_device_data(ip, auth)["panelLayout"]["layout"]["positionData"]

    def _set_stream_control_mode(self, ip: str, auth: str, version: int = 1):
        """
        Set the stream control mode to external control.
        """
        body = {
            "write": {
                "command": "display",
                "animType": "extControl",
                "extControlVersion": "v" + str(version),
            }
        }
        self._request("PUT", ip, auth, "effects", body)

    def _get_device_data(self, ip: str, auth: str) -> dict:
        """
        Gets panel info from the Nanoleaf controller.
        """
        return self._request("GET", ip, auth, "")

    def _send_stream_control_frames(self, frames: list[Frame], ip: str):
        """
        Sends a list of frames to the Nanoleaf controller.
        """
        stream = bytearray()
        # & 0xFF is used to convert the int to a byte
        stream.append(len(frames) & 0xFF)
        for frame in frames:
            stream.append(frame.panel_id & 0xFF)
            stream.append(1 & 0xFF)
            stream.append(frame.red & 0xFF)
            stream.append(frame.green & 0xFF)
            stream.append(frame.blue & 0xFF)
            stream.append(0 & 0xFF)
            stream.append(frame.transition_time & 0xFF)

        self._SOCK.sendto(stream, (ip, self._SOCK_PORT))

    def _map_panel_positions(self, controller_data: list[list[PhysicalPosition]]):
        """
        Creates a map of (row, col) values to Position objects based on the PhysicalPosition data.
        """
        self._panel_position_map: dict[tuple[int, int], Position] = {}
        for i, panels in enumerate(controller_data):
            for j, panel in enumerate(panels):
                row, col = data.panel_positions[i][j]
                self._panel_position_map[(row, col)] = Position(
                    row=row,
                    col=col,
                    controller_id=i,
                    panel_id=panel["panelId"],
                )

    def update(self, updates: list[PanelUpdate]):
        """
        Updates the display based on a list of updates.
        Panels not included will remain unchanged.
        """
        controller_frames = {i: [] for i in range(len(self.IPS))}
        for update in updates:
            position = self._panel_position_map[(update.row, update.col)]
            red, green, blue = utils.hex_to_rgb(update.color)
            frame = Frame(
                panel_id=position.panel_id,
                red=red,
                green=green,
                blue=blue,
                transition_time=update.transition_time,
            )
            controller_frames[position.controller_id].append(frame)

        for controller_id, frames in controller_frames.items():
            self._send_stream_control_frames(frames, self.IPS[controller_id])
