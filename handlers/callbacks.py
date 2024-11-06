from data.loader import bot
from telebot import types

@bot.callback_query_handler(func=lambda call: 'translation' in call.data)
def add_to_favourite(call: types.CallbackQuery):
    print(call.data)
    bot.answer_callback_query(call.id, 'Добавлено в избранное')
    start(call.message)
