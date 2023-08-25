from aiogram import Router, F, types

from keyboards import how_do_you_do

router = Router()


@router.message(F.text.lower() == "привет")
async def answer_to_hello(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Как дела?", reply_markup=how_do_you_do.keyboard)
