import asyncio
from aiogram import Bot, Dispatcher

from config import settings

# Объект бота
bot = Bot(token=settings.TOKEN)

# Объект диспетчера
dp = Dispatcher()


async def main():
    from handlers import dp
    await dp.start_polling(bot)


# Запуск скрипта
if __name__ == '__main__':
    asyncio.run(main())
