import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# ទាញយក Token ពី Environment Variable របស់ Railway
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# ពេល User វាយ /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # បង្កើតប៊ូតុងនៅខាងក្រោម (Reply Keyboard)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    
    # បង្កើតប៊ូតុងទីមួយ
    btn1 = KeyboardButton("TIK TOK LIKE KH")
    
    # ដាក់បញ្ចូលប៊ូតុង (បើចង់បានប៊ូតុងទី២ អាចបន្ថែម btn2)
    markup.add(btn1)
    
    bot.send_message(message.chat.id, "សួស្តី! សូមជ្រើសរើសសេវាកម្មខាងក្រោម៖", reply_markup=markup)

# ពេល User ចុចលើប៊ូតុង "TIK TOK LIKE KH"
@bot.message_handler(func=lambda message: message.text == "TIK TOK LIKE KH")
def handle_tiktok_like(message):
    bot.send_message(message.chat.id, "✅ អ្នកបានជ្រើសរើស TIK TOK LIKE KH។ សូមបញ្ចូន Link វីដេអូរបស់អ្នកមកកាន់ទីនេះ...")

print("Bot កំពុងដំណើរការ...")
bot.infinity_polling()
