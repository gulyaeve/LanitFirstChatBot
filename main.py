import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers import start, any_text, sticker, hello, cat
from config import settings


# Настройка логирования
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=settings.TOKEN)
# Объект диспетчера
dp = Dispatcher()

# Добавляем роутеры из хэндлеров в диспетчер
dp.include_routers(
    start.router,
    sticker.router,
    hello.router,
    cat.router,
)

# dp.include_router(start.router)
# dp.include_router(sticker.router)
# dp.include_router(hello.router)
dp.include_router(any_text.router)


async def main():
    await dp.start_polling(bot)


# Запуск скрипта
if __name__ == '__main__':
    asyncio.run(main())
