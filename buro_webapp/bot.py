import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = '7083425620:AAHaBufx9L-fcgAQ2ij7eGnyt2UyF4ArCLw'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text="Привет!.")

async def send_message_to_telegram(chat_id, message):
    await bot.send_message(chat_id=chat_id, text=message)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
