from data.loader import bot
from telebot import types
from keyboards.reply import start_kb
from database import db


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    chat_id = message.chat.id
    db.user.id, is_exists =  db.get_user_id(chat_id)
    if not is_exists:
        db.add_user()

    first_name = message.from_user.first_name
    msg = f'Привет, {first_name}. Добро пожаловать в бот переводчик.\nВыбери команду снизу ⬇'
    bot.send_message(chat_id, msg, reply_markup=start_kb())
