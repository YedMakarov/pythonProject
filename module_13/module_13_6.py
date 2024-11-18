# Задача "Ещё больше выбора".


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Reply Keyboard
kb = ReplyKeyboardMarkup(resize_keyboard=True)
bt1 = KeyboardButton(text="Рассчитать")
bt2 = KeyboardButton(text="Информация")
kb.add(bt1)
kb.add(bt2)

# Inline Keyboard
kbi = InlineKeyboardMarkup(resize_keyboard=True)
bti1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
bti2 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
kbi.row(bti1, bti2)


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kbi)


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()


@dp.message_handler(commands=["start"])
async def urban_messages(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


# @dp.message_handler(text="Рассчитать")
# async def set_age(message):
#     await message.answer("Введите свой возраст:")
#     await UserState.age.set()


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


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

"""
Упрощенный вариант формулы Миффлина-Сан Жеора:
для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
"""
