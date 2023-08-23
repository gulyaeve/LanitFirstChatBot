from aiogram import Router, F, types

router = Router()


@router.message(F.text.lower() == "привет")
async def answer_to_hello(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
