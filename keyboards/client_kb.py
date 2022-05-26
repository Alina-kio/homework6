from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

films_button = KeyboardButton("/films")

start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_markup.row(films_button)
