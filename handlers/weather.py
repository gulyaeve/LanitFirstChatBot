from aiogram import Router, types, F
from aiogram.filters import Command

from keyboards import location
from utils.weather_api import WeatherAPI

router = Router()

weather_api = WeatherAPI()


@router.message(Command("weather"))
async def get_weather(message: types.Message):
    await message.reply("Отправь мне свою геолокацию", reply_markup=location.keyboard)


@router.message(F.location)
async def answer_weather(message: types.Message):
    weather = await weather_api.get_weather_info(message.location.latitude, message.location.longitude)
    await message.answer(str(weather))
