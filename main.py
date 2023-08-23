import asyncio
from aiogram import Bot, Dispatcher
from handlers import start, any_text, sticker
from config import settings


async def main():
    # Объект бота
    bot = Bot(token=settings.TOKEN)
    # Объект диспетчера
    dp = Dispatcher()

    # Добавляем роутеры из хэндлеров в диспетчер
    dp.include_router(start.router)
    dp.include_router(sticker.router)
    dp.include_router(any_text.router)

    await dp.start_polling(bot)


# Запуск скрипта
if __name__ == '__main__':
    asyncio.run(main())
