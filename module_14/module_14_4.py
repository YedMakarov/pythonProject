# Задача "Продуктовая база".


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# import asyncio

import logging

from crud_functions import initiate_db, get_all_products

logging.basicConfig(level=logging.INFO)

# Инициализация и заполнение базы данных
initiate_db()
products = get_all_products()

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Reply Keyboard
kb = ReplyKeyboardMarkup(resize_keyboard=True)
bt1 = KeyboardButton(text="Рассчитать")
bt2 = KeyboardButton(text="Информация")
bt3 = KeyboardButton(text="Купить")
kb.row(bt1, bt2)
kb.add(bt3)

# Inline Keyboard
kbi = InlineKeyboardMarkup(resize_keyboard=True)
bti1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
bti2 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
bti3 = InlineKeyboardButton(text="Вернутся в главное меню", callback_data="back_to_main_menu")
kbi.row(bti1, bti2)
kbi.add(bti3)

kbi2 = InlineKeyboardMarkup(resize_keyboard=True)
bti2_1 = InlineKeyboardButton(text="Product1", callback_data="product_buying")
bti2_2 = InlineKeyboardButton(text="Product2", callback_data="product_buying")
bti2_3 = InlineKeyboardButton(text="Product3", callback_data="product_buying")
bti2_4 = InlineKeyboardButton(text="Product4", callback_data="product_buying")
kbi2.row(bti2_1, bti2_2, bti2_3, bti2_4)


@dp.message_handler(commands=["start"])
async def urban_messages(message):
    await message.answer(f"Привет, {message.from_user.username}! Я бот помогающий твоему здоровью.",
                         reply_markup=kb)


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kbi)


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    with open("files/vitamin_1.png", "rb") as img:
        # await message.answer_photo(img, "Название: Product1 | Описание 1 | Цена: 100 ")
        await message.answer_photo(img, f'Название: {products[0][1]} | Описание: {products[0][2]} | '
                                        f'Цена: {products[0][3]}')

    with open("files/vitamin_2.png", "rb") as img:
        # await message.answer_photo(img, "Название: Product2 | Описание 2 | Цена: 200 ")
        await message.answer_photo(img, f'Название: {products[1][1]} | Описание: {products[1][2]} | '
                                        f'Цена: {products[1][3]}')

    with open("files/vitamin_3.png", "rb") as img:
        # await message.answer_photo(img, "Название: Product3 | Описание 3 | Цена: 300 ")
        await message.answer_photo(img, f'Название: {products[2][1]} | Описание: {products[2][2]} | '
                                        f'Цена: {products[2][3]}')

    with open("files/vitamin_4.png", "rb") as img:
        # await message.answer_photo(img, "Название: Product4 | Описание 4 | Цена: 400 ")
        await message.answer_photo(img, f'Название: {products[3][1]} | Описание: {products[3][2]} | '
                                        f'Цена: {products[3][3]}')

    await message.answer("Выберите продукт для покупки:", reply_markup=kbi2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(msg_age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(msg_growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(msg_weight=message.text)
    data = await state.get_data()

    calories = (10 * int(data['msg_weight']) + 6.25 * int(data['msg_growth'])
                - 5 * int(data['msg_age']) + 5)

    await message.answer(f"Доступное количество петребления килокалорий - {calories}.")
    await state.finish()


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()


@dp.callback_query_handler(text="back_to_main_menu")
async def back(call):
    await call.message.answer("Вы снова в главном меню:", reply_markup=kb)
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
