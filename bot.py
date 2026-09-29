import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("🛍️ សេវាកម្ម")
    markup.add(btn1)
    bot.send_message(message.chat.id, "សួស្តី! សូមជ្រើសរើសជម្រើសខាងក្រោម៖", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🛍️ សេវាកម្ម")
def show_services(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_tiktok = KeyboardButton("Tik Tok Like KH")
    btn_back = KeyboardButton("⬅️ ត្រឡប់ក្រោយ")
    markup.add(btn_tiktok)
    markup.add(btn_back)
    bot.send_message(message.chat.id, "សូមជ្រើសរើសសេវាកម្មខាងក្រោម៖", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Tik Tok Like KH")
def handle_tiktok_like(message):
    bot.send_message(message.chat.id, "កំពុងរៀបចំប្រព័ន្ធ ⚙️")

@bot.message_handler(func=lambda message: message.text == "⬅️ ត្រឡប់ក្រោយ")
def handle_back(message):
    send_welcome(message)

print("Bot កំពុងដំណើរការ...")
bot.infinity_polling()
