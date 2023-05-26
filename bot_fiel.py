
import logging

from aiogram import Bot, Dispatcher, executor, types
from search_wiki import get_wiki_page

API_TOKEN = '6109912254:AAERiLoRhCtPH3payGJys0PDIrxbOKC0xM8'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
    types.KeyboardButton("Айпи главного админа")
)
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет я Sheridn13")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("ням\nамням\nамня амням")
    await message.reply("перевод\nПривет\nЯ бот википедия!\nМогу разговаривать на языке амням",reply_markup=menu)

@dp.message_handler(text="Айпи главного админа")
async def echo(message: types.Message):   
    await message.answer("😎@Mr_turba")

@dp.message_handler(content_types=['text'])
async def user_text_handler(message: types.Message):
    user_text = message.text
    result = get_wiki_page(user_text)
    if result:
        await message.answer(result)
    else:
        await message.answer("☹️")
        await message.answer("😐Извените но я не нашол нужной информации😐")




@dp.message_handler(content_types=['sticker'])
async def user_text_handler(message: types.Message):
    await message.answer("sticker")


    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)