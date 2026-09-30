import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# ទាញយក Token ពី Environment Variable របស់ Railway
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# ពេល User វាយ /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # បង្កើតផ្ទាំងប៊ូតុង
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    
    # បង្កើតប៊ូតុងទាំង៣
    btn1 = KeyboardButton("🛍️ Shop Services")
    btn2 = KeyboardButton("👨🏻‍💻 Support")
    btn3 = KeyboardButton("📥 Total oder")
    
    # រៀបចំប៊ូតុង (btn1 នៅជួរទី១ | btn2 និង btn3 នៅជួរទី២ ទន្ទឹមគ្នា)
    markup.add(btn1)
    markup.add(btn2, btn3)
    
    bot.send_message(message.chat.id, "សួស្តី! សូមជ្រើសរើសជម្រើសខាងក្រោម៖", reply_markup=markup)

# ពេល User ចុចលើប៊ូតុង "🛍️ Shop Services"
@bot.message_handler(func=lambda message: message.text == "🛍️ Shop Services")
def handle_shop(message):
    bot.send_message(message.chat.id, "សូមស្វាគមន៍មកកាន់សេវាកម្មរបស់យើង! តើមានអ្វីឱ្យខ្ញុំជួយ? 🛒")

# ពេល User ចុចលើប៊ូតុង "👨🏻‍💻 Support"
@bot.message_handler(func=lambda message: message.text == "👨🏻‍💻 Support")
def handle_support(message):
    bot.send_message(message.chat.id, "ត្រូវការជំនួយមែនទេ? សូមទម្លាក់សំណួររបស់អ្នកនៅទីនេះ... 💬")

# ពេល User ចុចលើប៊ូតុង "📥 Total oder"
@bot.message_handler(func=lambda message: message.text == "📥 Total oder")
def handle_total_order(message):
    bot.send_message(message.chat.id, "កំពុងពិនិត្យមើលចំនួន Order សរុបរបស់អ្នក... 📦")

print("Bot កំពុងដំណើរការ...")
bot.infinity_polling()
