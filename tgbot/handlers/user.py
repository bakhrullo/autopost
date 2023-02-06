from aiogram import Dispatcher
from aiogram.types import Message


async def user_start(message: Message):
    print(message)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
