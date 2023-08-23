import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config import settings

# Объект бота
bot = Bot(token=settings.TOKEN)

# Объект диспетчера
dp = Dispatcher()


# Хэндлер на команду старт
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


async def main():
    await dp.start_polling(bot)


# Запуск скрипта
if __name__ == '__main__':
    asyncio.run(main())
