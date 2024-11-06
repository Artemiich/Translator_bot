from data.loader import bot, translator
from telebot import types
from keyboards.reply import (lang_kb)
from googletrans import LANGCODES
from database import db

@bot.message_handler(func=lambda msg: msg.text == 'Перевод')
def start_translation(message: types.Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Выберите язык, с которого хотите сделать перевод',
                     reply_markup=lang_kb())
    bot.register_next_step_handler(message, get_lang_from)



def get_lang_from(message: types.Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Выберите язык, на который хотите сделать перевод',
                     reply_markup=lang_kb())
    bot.register_next_step_handler(message, get_lang_to, message.text)

def get_lang_to(message: types.Message, lang_from):
    print('lang_from', lang_from)
    print('lang_to', message.text)
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Напишите слово или текст для перевода', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, translate, lang_from, message.text)

def translate(message: types.Message, lang_from: str, lang_to: str):
    code_from = LANGCODES.get(lang_from)
    code_to = LANGCODES.get(lang_to)
    text = message.text
    translated_text = translator.translate(text, code_to, code_from).text
    db.add_translation(
        original=message.text,
        translated=translated_text,
        code_from=code_from,
        code_to=code_to,
        chat_id=message.chat.id
    )
    msg = f"""
Оригинал: <b>{text}<b>
Перевод: <b>{translated_text}<b>
С какого: <b>{code_from}<b>
На какой: <b>{code_to}<b>
"""
    bot.send_message(message.chat.id, msg, parse_mode='HTML')


@bot.message_handler(func=lambda msg: msg.text == 'История')
def history(message: types.Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Ваша история переводов')














