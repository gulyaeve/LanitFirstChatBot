from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

form_router = Router()


class Form(StatesGroup):
    name = State()
    age = State()
    city = State()


@form_router.message(F.text == "давай дружить")
async def question_name(message: types.Message, state: FSMContext):
    # Переключение состояния
    await state.set_state(Form.name)
    await message.answer("Ок, напиши своё имя:", reply_markup=types.ReplyKeyboardRemove())


@form_router.message(Form.name)
async def save_name(message: types.Message, state: FSMContext):
    name = message.text
    with open("names.txt", "w") as file:
        file.write(name)

    await state.set_state(Form.age)
    await message.answer("Имя записал, теперь скажи сколько тебе лет?")


@form_router.message(Form.age)
async def save_age(message: types.Message, state: FSMContext):
    age = message.text
    if age.isdigit():
        age = int(age)
        if age < 0 or age > 99:
            return await message.reply("Я не верю что тебе столько лет!")
        else:
            await state.set_state(Form.city)
            await message.answer("Очень хорошо, напиши где ты живешь?")
    else:
        return await message.reply("Введи, пожалуйста, число!")


@form_router.message(Form.city)
async def save_city(message: types.Message, state: FSMContext):
    city = message.text
    with open("cities.txt", "w") as file:
        file.write(city)

    await state.clear()
    await message.answer("Круто! Я теперь про тебя всё знаю)")



