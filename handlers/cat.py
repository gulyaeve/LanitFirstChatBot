from aiogram import Router, types
from aiogram.filters import Command

from utils.base_api import BaseAPI

router = Router()
cat_api = BaseAPI("https://cataas.com")


@router.message(Command("cat"))
async def get_cat_picture(message: types.Message):
    cat_pic = await cat_api.get_data("/cat")
    await message.reply_photo(types.BufferedInputFile(cat_pic, "cat.png"))
