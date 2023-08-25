from typing import Any

from aiogram import Router, types, F
from aiogram.handlers import CallbackQueryHandler

router = Router()


@router.callback_query(F.data == "1")
async def start_button(callback: types.CallbackQuery):
    await callback.answer("You start misson", show_alert=True)


# @router.callback_query(F.data == "2")
# class StartHandler(CallbackQueryHandler):
#     async def handle(self) -> Any:
#         await self.message.reply("222")


@router.callback_query(F.data == "2")
async def stop_button(callback: types.CallbackQuery):
    await callback.answer("You stop misson")

