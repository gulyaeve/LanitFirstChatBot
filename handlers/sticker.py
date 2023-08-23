from aiogram import Router, types, F

router = Router()


@router.message(F.sticker)
async def answer_sticker(message: types.Message):
    await message.answer_sticker(message.sticker.file_id)
