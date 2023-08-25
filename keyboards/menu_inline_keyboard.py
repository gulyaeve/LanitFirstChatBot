from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, LoginUrl

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Start",
                callback_data="1"
            ),
            InlineKeyboardButton(
                text="yandex",
                url="https://ya.ru"
            ),
        ],
        [
            InlineKeyboardButton(
                text="stop",
                callback_data="2"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Аккаунт моего создателя",
                url="tg://user?id=253122"
            ),
        ],

    ],
)
