import logging

from aiogram import types, Router
from aiogram.filters import Command

from keyboards import menu_inline_keyboard
from middlewares.counter import LoggingMiddleware

router = Router()
router.message.middleware(LoggingMiddleware())


# Хэндлер на команду старт
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!", reply_markup=menu_inline_keyboard.inline_keyboard)
