import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from handlers import start, any_text, sticker, hello, cat, weather, inline_menu, FSM_example, cancel
from config import settings
from middlewares import log_update
from utils.commands import set_up_default_commands


# Настройка логирования
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=settings.TOKEN)
# Объект диспетчера
dp = Dispatcher()

dp.include_router(cancel.router)
dp.include_router(log_update.router)
# Добавляем роутеры из хэндлеров в диспетчер
dp.include_routers(
    start.router,
    sticker.router,
    hello.router,
    cat.router,
    weather.router,
    inline_menu.router,
    FSM_example.form_router
)

dp.include_router(any_text.router)


async def main():
    await set_up_default_commands(bot)
    await dp.start_polling(bot)


# Запуск скрипта
if __name__ == '__main__':
    asyncio.run(main())
