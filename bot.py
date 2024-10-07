from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = " :) "
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())



@dp.message_handler(text = ['Hello', 'Hi'])
async def Vlad_massage(message):
    print("Vlad message")
    await message.answer("Привет дорогой друг!")

@dp.message_handler(commands = ['start'])
async def start_massage(message):
    print("Start message")
    await message.answer("Рад видеть тебя в нашем боте!")

@dp.message_handler()
async def all_massage(message):
    print("Мы получили сообщение!")
    await message.answer(message.text.upper())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)