
from telebot import TeleBot
from googletrans import Translator
import settings

bot = TeleBot(token=settings.BOT_TOKEN)


translator = Translator()