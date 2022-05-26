import imp
from aiogram import types, Dispatcher
from config import bot, dp
from parser import film
from keyboards import client_kb


async def start(message: types.Message):
    await message.answer(f"Hi, my friend {message.from_user.full_name}",
                                reply_markup=client_kb.start_markup)


async def parser_films(message: types.Message):
    data = film.parser()
    for item in data:
        await bot.send_message(message.chat.id, 
                                        f"{item['title']}\n\n"
                                        f"{item['entity']}\n"
                                        f"{item['link']}\n")
                                        # f"{item['photo']}")


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(parser_films, commands=['films'])
