# import the module
import string
from tokenize import String
from xmlrpc.client import Boolean, boolean
from datetime import datetime
import python_weather
import asyncio
import os

async def getweather(self):
  # declare the client. format defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(format=python_weather.METRIC) as client:

    # fetch a weather forecast from a city
    weather = await client.get("Calgary, Alberta")

    # returns the current day's forecast temperature (int)
    now = datetime.now()
    now = now.hour
    self.dark_mode = False
    self.temp_is_negative = False
    self.temp_first = weather.current.temperature // 10
    self.temp_second = weather.current.temperature % 10
    if(weather.current.temperature < 0):
      self.temp_is_negative = True

    if(now > 17):
      self.dark_mode = True

    weather_description = weather.current.description
    if('PARTLY' in (weather_description.upper()) and 'CLOUDY' in (weather_description.upper())):
      self.temp_condition = "party cloudy"

    if('CLOUD' in (weather_description.upper())):
      self.temp_condition = "cloudy"

    elif('SNOW'in (weather_description.upper())):
      self.temp_condition = "snowy"

    elif('RAIN'in (weather_description.upper())):
      self.temp_condition = "rainy"

    else:
      self.temp_condition = "sunny"

    weather_humidity = weather.current.humidity
    weather_feel_like = weather.current.feels_like


class Weather:
  dark_mode: Boolean
  temp_first: int
  temp_second: int
  temp_condition: string
  temp_is_negative: Boolean

  def __init__(self):
    if os.name == "nt":
      asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather(self))
