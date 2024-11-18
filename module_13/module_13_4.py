# Задача "Цепочка вопросов".


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = "5217972794:AAGBjukG7mwtgfzV5I94Vwiz5eBd70TLJFg"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text="Calories")
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


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
    print(f"data - {data}")

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
