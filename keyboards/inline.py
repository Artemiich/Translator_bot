from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def add_to_favourite_kb(translation_id=0):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton(text='Добавить в избранное',
                             callback_data=f'translation_{translation_id}'),
    )
    return kb







