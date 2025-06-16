from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor
from database import init_db
import asyncio

API_TOKEN = '1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ'  # ← ЗАМЕНИТЬ НА СВОЙ ТОКЕН!
WEBAPP_URL = 'https://yourdomain.com'   # ← ЗАМЕНИТЬ НА СВОЙ URL

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    web_app = WebAppInfo(url=f"{WEBAPP_URL}?user_id={message.from_user.id}")
    keyboard.add(InlineKeyboardButton(text="🎁 Выбрать подарок", web_app=web_app))
    await message.answer("Нажмите, чтобы выбрать подарок:", reply_markup=keyboard)

if __name__ == '__main__':
    init_db()
    from api import app
    import uvicorn
    print("Запуск бота и веб-сервера...")
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling())
    loop.run_until_complete(uvicorn.run(app, host='0.0.0.0', port=8080))