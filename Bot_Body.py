import json
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import hbold, hlink
from aiogram.dispatcher.filters import Text
from main import get_data_selenium
import os

#передача токена из батника
bot = Bot(token=os.getenv("TOKEN"), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ['Актуальные туры', 'Товары для отдыха', 'В разработке...']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Здесь все, чтобы отдохнуть, как у вас с деньгами?", reply_markup=keyboard)

@dp.message_handler(Text(equals='Актуальные туры'))
async def get_tours(message: types.Message):
    await message.answer("Секундочку, грузим актуальные туры...")

    get_data_selenium()
    with open('hotels.json') as file:
        data = json.load(file)
    for item in data:
        card = f"{hlink(item.get('arrival'), item.get('URL'))}\n" \
            f"{hbold('Название отеля: ')} {item.get('hotel_name')}\n" \
            f"{hbold('Перелет: ')} {item.get('direction')}\n" \
            f"{hbold('Ценник: ')} {item.get('price')}\n" \

        await message.answer(card)


def main():
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    main()


