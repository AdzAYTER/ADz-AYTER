import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import os

# ប្រើ Environment Variable សម្រាប់សុវត្ថិភាព Token នៅលើ Railway
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'ដាក់_TOKEN_របស់អ្នកនៅទីនេះ')
bot = telebot.TeleBot(BOT_TOKEN)

# បង្កើតផ្ទាំងចុចបញ្ជា (Main Menu) ថ្មី ដែលមាន ៤ ប៊ូតុង
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton('🛍️ TOPUP NOW')
    btn2 = KeyboardButton('👨🏻‍‍💻ACCOUNT')
    btn3 = KeyboardButton('💬Support 24/7')
    btn4 = KeyboardButton('💸 ដាក់ប្រាក់')
    
    markup.add(btn1)          # ជួរទី១
    markup.add(btn2, btn4)    # ជួរទី២ (គណនី និង ដាក់ប្រាក់)
    markup.add(btn3)          # ជួរទី៣
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, 
        "សួស្ដី! សូមស្វាគមន៍មកកាន់សេវាកម្មរបស់យើង។", 
        reply_markup=main_menu()
    )

# មុខងារសម្រាប់ប៊ូតុង 🛍️ TOPUP NOW
@bot.message_handler(func=lambda message: message.text == '🛍️ TOPUP NOW')
def topup_menu(message):
    markup = InlineKeyboardMarkup(row_width=1)
    games = ["Free Fire", "Mobile legends", "Roblox", "Honor of King"]
    
    # បង្កើតប៊ូតុងសម្រាប់ហ្គេមនីមួយៗ
    for game in games:
        markup.add(InlineKeyboardButton(game, callback_data='out_of_stock'))
        
    bot.send_message(message.chat.id, "សូមជ្រើសរើសហ្គេមខាងក្រោម៖", reply_markup=markup)

# មុខងារបង្ហាញសារ "អស់ស្ដុកទាំងអស់" នៅពេលចុចលើហ្គេម
@bot.callback_query_handler(func=lambda call: call.data == 'out_of_stock')
def handle_out_of_stock(call):
    bot.answer_callback_query(call.id, "អស់ស្ដុកទាំងអស់", show_alert=True)

# មុខងារសម្រាប់ប៊ូតុង 👨🏻‍💻ACCOUNT
@bot.message_handler(func=lambda message: message.text == '👨🏻‍💻ACCOUNT')
def account_info(message):
    user = message.from_user
    name = user.first_name
    username = f"@{user.username}" if user.username else "គ្មាន Username"
    user_id = user.id
    balance = "$0.00" # ទឹកប្រាក់កំណត់ជាគំរូ
    rank = "សមាជិកថ្មី" # កម្រិតអ្នកទិញ
    
    text = (f"» ឈ្មោះ Telegram: {name}\n"
            f"» Username: {username}\n"
            f"» User ID: {user_id}\n"
            f"» Balance: {balance}\n"
            f"» Rank អ្នកទិញ: {rank}")
    bot.send_message(message.chat.id, text)

# មុខងារសម្រាប់ប៊ូតុង 💸 ដាក់ប្រាក់ (ថ្មី)
@bot.message_handler(func=lambda message: message.text == '💸 ដាក់ប្រាក់')
def deposit_info(message):
    # សូមផ្លាស់ប្ដូរ Link ខាងក្រោមនេះ ទៅជា Link រូបភាព KHQR ពិតប្រាកដរបស់អ្នក
    khqr_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/QR_code_for_mobile_English_Wikipedia.svg/1200px-QR_code_for_mobile_English_Wikipedia.svg.png" 
    
    caption_text = ("» ផ្ញើរប្រតិបត្ដការចូលក្នុងបត!\n"
                    "» រងចាំការត្រូតពិនិត្យពីអ្នកគ្រប់គ្រង")
    
    try:
        # ផ្ញើរូបថត KHQR ព្រមទាំងសារនៅខាងក្រោមរូប
        bot.send_photo(message.chat.id, photo=khqr_image_url, caption=caption_text)
    except Exception as e:
        # ប្រសិនបើ Link រូបភាពមានបញ្ហា វានឹងលោតជាសារអក្សរជំនួសវិញ
        bot.send_message(message.chat.id, "[រូបថត KHQR]\n\n" + caption_text)

# មុខងារសម្រាប់ប៊ូតុង 💬Support 24/7
@bot.message_handler(func=lambda message: message.text == '💬Support 24/7')
def support_info(message):
    text = ("ផ្ដល់ជំនួយជូនលោកអ្នកឆាប់រហ័ស\n"
            "» @ADzAYTER\n"
            "» @LongzzSMMDIGItaLL")
    bot.send_message(message.chat.id, text)

# ចាប់ផ្ដើមដំណើរការ Bot
if __name__ == "__main__":
    print("Bot កំពុងដំណើរការ...")
    bot.infinity_polling()
