from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='5045920634:AAEov1VyqVt1OFh5Y_hYfUJPRcaB9Qx7XI0')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! \nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.reply("Напиши мне что-ниубудь, а я отправлю тебе это в ответ!")


@dp.message_handler()
async def echo_massage(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Я не понял, что вы хотели.\nНапишите команду /help")


if __name__ == '__main__':
    print("Бот запущен")
    executor.start_polling(dp)