# import the module
import python_weather
import asyncio
import os

async def getweather():
  # declare the client. format defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(format=python_weather.METRIC) as client:

    # fetch a weather forecast from a city
    weather = await client.get("Calgary, Alberta")

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)
    print(weather.current.description)
    print(weather.current.humidity)
    print(weather.current.feels_like)

if __name__ == "__main__":
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details

  if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(getweather())
