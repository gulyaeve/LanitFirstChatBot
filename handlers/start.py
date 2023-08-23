from aiogram import types
from aiogram.filters import CommandStart

from main import dp


# Хэндлер на команду старт
@dp.message(CommandStart)
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
