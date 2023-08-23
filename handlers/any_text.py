from aiogram import types
from aiogram import F

from main import dp


@dp.message(F.text)
async def answer_to_any_text(message: types.Message):
    await message.reply(message.text)
