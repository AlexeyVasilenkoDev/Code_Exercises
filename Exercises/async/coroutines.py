import asyncio
import inspect
import pprint
import random

import requests
from geonamescache import GeonamesCache


async def get_random_city():
    gc = GeonamesCache()
    city = random.choice(list(gc.get_cities().items()))[1]["name"]
    # print(city)
    return city


async def get_weather_podcast(future, date):
    print("Starting coroutine!")
    while True:
        city = await get_random_city()
        weather_forecast = requests.get(
            f"https://api.weatherapi.com/v1/future.json?"
            f"key=f5ac2565c90745acb59181224220611&"
            f"q={city}&"
            f"dt={date}").json()
        if list(dict(weather_forecast).keys())[0] == "location" and city == (dict(weather_forecast))["location"][
            "name"]:
            # print(weather_forecast)
            print(f"{inspect.stack()[0][3]} function finished")
            weather_dict = {"City": city,
                            "Date": weather_forecast["forecast"]["forecastday"][0]["hour"][5]["time"],
                            "Degrees": weather_forecast["forecast"]["forecastday"][0]["day"]["avgtemp_c"],
                            # I know how bad it looks like, but it still works
                            "Rain": weather_forecast["forecast"]["forecastday"][0]["hour"][5]["will_it_rain"]}
            # pprint.pprint(weather_dict)
            future.set_result(weather_dict)
            return weather_dict, date


async def choose_suitable_clothes(future):
    clothes_dict = {
        "Hot": "T-shirt and shirts",
        "Medium": "Hoodie and jeans",
        "Cold": "Jacket and warm pants"
    }
    result = await future
    print(result)
    if result['Degrees'] > 20:
        clothes = "T-shirt with shorts"
    elif 10 <= result['Degrees'] <= 20:
        clothes = "Hoodie with jeans"
    else:
        clothes = "Jacket with warm pants"
    clothes_choice = f"You should wear {clothes} " \
                     f"{'and don`t forget to take an umbrella ' if result['Rain'] else ''}" \
                     f"if you want to visit {result['City']} on {result['Date']}"
    print(clothes_choice)
    # pprint.pprint(result)
    print(f"{inspect.stack()[0][3]} function finished")


async def end_process(loop):
    print(f"{inspect.stack()[0][3]} function finished")
    loop.stop()
    print("Event loop ended!")


fut = asyncio.Future()
event_loop = asyncio.get_event_loop()

event_loop.create_task(get_weather_podcast(fut, "2022-12-31"))
event_loop.create_task(choose_suitable_clothes(fut))
event_loop.create_task(end_process(event_loop))

event_loop.run_forever()
event_loop.close()
