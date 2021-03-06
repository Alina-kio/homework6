from aiogram.utils import executor
from config import dp
from hendlers import client
import logging


client.register_handler_client(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
