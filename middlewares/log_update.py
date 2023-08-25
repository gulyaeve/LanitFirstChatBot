import logging

from aiogram import BaseMiddleware, Router
from aiogram.types import Update, Message


class CounterMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
        self,
        handler,
        event: Message,
        data
    ):
        print(event)
        return await handler(event, data)


router = Router()
router.message.middleware(CounterMiddleware())
