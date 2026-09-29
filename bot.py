import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# ទាញយក Token ពី Environment Variable របស់ Railway
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# ១. ម៉ឺនុយដើម ពេល User វាយ /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    # បង្កើតប៊ូតុងសេវាកម្ម
    btn1 = KeyboardButton("🛍️ សេវាកម្ម")
    markup.add(btn1)
    
    bot.send_message(message.chat.id, "សួស្តី! សូមជ្រើសរើសជម្រើសខាងក្រោម៖", reply_markup=markup)

# ២. ពេល User ចុចលើប៊ូតុង "🛍️ សេវាកម្ម" (ចូលម៉ឺនុយរង)
@bot.message_handler(func=lambda message: message.text == "🛍️ សេវាកម្ម")
def show_services(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    # បង្កើតប៊ូតុងខាងក្នុងសេវាកម្ម
    btn_tiktok = KeyboardButton("Tik Tok Like KH")
    btn_back = KeyboardButton("⬅️ ត្រឡប់ក្រោយ")
    
    # រៀបចំប៊ូតុង (មួយជួរមានមួយ ឬពីរ តាមការ add)
    markup.add(btn_tiktok)
    markup.add(btn_back)
    
    bot.send_message(message.chat.id, "សូមជ្រើសរើសសេវាកម្មខាងក្រោម៖", reply_markup=markup)

# ៣. ពេល User ចុចលើប៊ូតុង "Tik Tok Like KH"
@bot.message_handler(func=lambda message: message.text == "Tik Tok Like KH")
def handle_tiktok_like(message):
    bot.send_message(message.chat.id, "កំពុងរៀបចំប្រព័ន្ធ ⚙️")

# ៤. ពេល User ចុចលើប៊ូតុង "⬅️ ត្រឡប់ក្រោយ"
@bot.message_handler(func=lambda message: message.text == "⬅️ ត្រឡប់ក្រោយ")
def handle_back(message):
    send_welcome(message) # ហៅ function send_welcome មកវិញ ដើម្បីបង្ហាញម៉ឺនុយដើម

print("Bot កំពុងដំណើរការ...")
bot.infinity_polling()
