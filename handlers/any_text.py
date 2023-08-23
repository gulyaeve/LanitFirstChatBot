from aiogram import types, Router, F

router = Router()


@router.message(F.text)
async def answer_to_any_text(message: types.Message):
    await message.reply(message.text)
