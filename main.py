import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values
from aiogram.filters import Command
from random import choice

names = ('dfs', 'dsfs', 'sdfs')
token = dotenv_values('.env')['TOKEN']
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message:types.Message):
    await message.answer(f'hello {message.from_user.first_name}')


@dp.message(Command('myinfo'))
async def my_info(message: types.Message):
    await message.answer(f'ur data:\nid:{message.from_user.id}\nfirst_name:{message.from_user.first_name}\nusername:{message.from_user.username}')


@dp.message(Command('random'))
async def random(message: types.Message):
    await message.answer(f'{choice(names)}')


async def main():
    await dp.start_polling(bot)


if __name__=='__main__':
    asyncio.run(main())
