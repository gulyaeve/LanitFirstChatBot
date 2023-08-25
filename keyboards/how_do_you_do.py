from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет"),
        ],
        [
            KeyboardButton(text="Ок"),
            KeyboardButton(text="Норм"),
        ],
        [
            KeyboardButton(text="Плохо"),
            KeyboardButton(text="Грустно("),
            KeyboardButton(text="Сойдёт"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
