from aiogram import types, Router
from aiogram.filters import Command

router = Router()


# Хэндлер на команду старт
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
