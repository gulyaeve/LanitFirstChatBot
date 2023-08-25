from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="Моя геолокация 📍",
                request_location=True,
            ),

        ],

    ],
    resize_keyboard=True,
    input_field_placeholder="Используй кнопку:",
)
