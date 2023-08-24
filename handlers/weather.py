from aiogram import Router, types, F
from aiogram.filters import Command

from utils.weather_api import WeatherAPI

router = Router()

weather_api = WeatherAPI()


@router.message(Command("weather"))
async def get_weather(message: types.Message):
    await message.reply("Отправь мне свою геолокацию")


@router.message(F.location)
async def answer_weather(message: types.Message):
    weather = await weather_api.get_weather_info(message.location.latitude, message.location.longitude)
    await message.answer(str(weather))
