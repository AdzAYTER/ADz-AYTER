import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# ==========================================
# ១. ម៉ឺនុយដើម (ពេលវាយ /start ឬចុចត្រឡប់ក្រោយ)
# ==========================================
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = KeyboardButton("🛍️ Shop Services")
    btn2 = KeyboardButton("👨🏻‍💻 Support")
    btn3 = KeyboardButton("📥 Total oder")
    
    markup.add(btn1)
    markup.add(btn2, btn3)
    
    bot.send_message(message.chat.id, "សួស្តី! សូមជ្រើសរើសជម្រើសខាងក្រោម៖", reply_markup=markup)


# ==========================================
# ២. ពេលចុច "🛍️ Shop Services" ចូលម៉ឺនុយរង
# ==========================================
@bot.message_handler(func=lambda message: message.text == "🛍️ Shop Services")
def show_shop_services(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    
    # បង្កើតប៊ូតុងសេវាកម្ម
    btn_gemini = KeyboardButton("1 Gemini Pro 18$/m")
    btn_chatgpt = KeyboardButton("2 Chat GPT Plus")
    btn_back = KeyboardButton("⬅️ ត្រឡប់ក្រោយ")
    
    # រៀបចំប៊ូតុង
    markup.add(btn_gemini)
    markup.add(btn_chatgpt)
    markup.add(btn_back)
    
    bot.send_message(message.chat.id, "សូមជ្រើសរើសសេវាកម្មដែលអ្នកចង់ទិញ៖", reply_markup=markup)


# ==========================================
# ៣. ពេលចុចសេវាកម្ម Gemini ឬ Chat GPT
# ==========================================
@bot.message_handler(func=lambda message: message.text in ["1 Gemini Pro 18$/m", "2 Chat GPT Plus"])
def handle_out_of_stock(message):
    # មិនថាគេចុចមួយណាទេ គឺចេញសារដូចគ្នា
    bot.send_message(message.chat.id, "សុំទោស អស់ស្ដុកហើយបង ❌")


# ==========================================
# ៤. ពេលចុចប៊ូតុងផ្សេងៗទៀត (Support, Total Order, ត្រឡប់ក្រោយ)
# ==========================================
@bot.message_handler(func=lambda message: message.text == "⬅️ ត្រឡប់ក្រោយ")
def handle_back(message):
    send_welcome(message) # ត្រឡប់ទៅម៉ឺនុយដើមវិញ

@bot.message_handler(func=lambda message: message.text == "👨🏻‍💻 Support")
def handle_support(message):
    bot.send_message(message.chat.id, "ត្រូវការជំនួយមែនទេ? សូមទម្លាក់សំណួររបស់អ្នកនៅទីនេះ... 💬")

@bot.message_handler(func=lambda message: message.text == "📥 Total oder")
def handle_total_order(message):
    bot.send_message(message.chat.id, "កំពុងពិនិត្យមើលចំនួន Order សរុបរបស់អ្នក... 📦")


print("Bot កំពុងដំណើរការ...")
bot.infinity_polling()
