import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import os

# ប្រើ Environment Variable សម្រាប់សុវត្ថិភាព Token នៅលើ Railway
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'ដាក់_TOKEN_របស់អ្នកនៅទីនេះ')
bot = telebot.TeleBot(BOT_TOKEN)

# កំណត់ឈ្មោះប៊ូតុងជាអថេរ (Variables) ដើម្បីការពារការខុសអក្ខរាវិរុទ្ធ ឬខុស Emoji
BTN_TOPUP = '🛍️ TOPUP NOW'
BTN_ACCOUNT = '👨🏻‍💻 ACCOUNT'
BTN_DEPOSIT = '💸 ដាក់ប្រាក់'
BTN_SUPPORT = '💬 Support 24/7'

# បង្កើតផ្ទាំងចុចបញ្ជា (Main Menu)
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    markup.add(KeyboardButton(BTN_TOPUP))                  # ជួរទី១
    markup.add(KeyboardButton(BTN_ACCOUNT), KeyboardButton(BTN_DEPOSIT))  # ជួរទី២
    markup.add(KeyboardButton(BTN_SUPPORT))                # ជួរទី៣
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, 
        "សួស្ដី! សូមស្វាគមន៍មកកាន់សេវាកម្មរបស់យើង។", 
        reply_markup=main_menu()
    )

# មុខងារសម្រាប់ប៊ូតុង 🛍 TOPUP NOW
@bot.message_handler(func=lambda message: message.text == BTN_TOPUP)
def topup_menu(message):
    markup = InlineKeyboardMarkup(row_width=1)
    games = ["Free Fire", "Mobile legends", "Roblox", "Honor of King"]
    
    for game in games:
        markup.add(InlineKeyboardButton(game, callback_data='out_of_stock'))
        
    bot.send_message(message.chat.id, "សូមជ្រើសរើសហ្គេមខាងក្រោម៖", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'out_of_stock')
def handle_out_of_stock(call):
    bot.answer_callback_query(call.id, "អស់ស្ដុកទាំងអស់", show_alert=True)

# មុខងារសម្រាប់ប៊ូតុង 👨🏻‍💻 ACCOUNT
@bot.message_handler(func=lambda message: message.text == BTN_ACCOUNT)
def account_info(message):
    user = message.from_user
    name = user.first_name
    username = f"@{user.username}" if user.username else "គ្មាន Username"
    user_id = user.id
    balance = "$0.00" 
    rank = "សមាជិកថ្មី" 
    
    text = (f"» ឈ្មោះ Telegram: {name}\n"
            f"» Username: {username}\n"
            f"» User ID: {user_id}\n"
            f"» Balance: {balance}\n"
            f"» Rank អ្នកទិញ: {rank}")
    bot.send_message(message.chat.id, text)

# មុខងារសម្រាប់ប៊ូតុង 💸 ដាក់ប្រាក់
@bot.message_handler(func=lambda message: message.text == BTN_DEPOSIT)
def deposit_info(message):
    # សូមផ្លាស់ប្ដូរ Link ខាងក្រោមនេះ ទៅជា Link រូបភាព KHQR ពិតប្រាកដរបស់អ្នក
    khqr_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/QR_code_for_mobile_English_Wikipedia.svg/1200px-QR_code_for_mobile_English_Wikipedia.svg.png" 
    
    caption_text = ("« សូមស្កេនទូរទាត់ប្រាក់គ្រប់ធនាគា»\n"
                    "» Game TopUp : \n"
                    "» QTY : (ចំនួនទំនិញ)\n"
                    "» Price : (តម្លៃទំនិញសរុប)\n"
                    "»»»»»»»»»«««««\n"
                    "បន្ទាប់ទូរទាត់រួច សូមផ្ញើរវិក័យបត្រមកកាន់បត💖🎉")
    
    try:
        bot.send_photo(message.chat.id, photo=khqr_image_url, caption=caption_text)
    except Exception as e:
        bot.send_message(message.chat.id, "[រូបថត KHQR]\n\n" + caption_text)

# មុខងារសម្រាប់ប៊ូតុង 💬 Support 24/7
@bot.message_handler(func=lambda message: message.text == BTN_SUPPORT)
def support_info(message):
    text = ("ផ្ដល់ជំនួយជូនលោកអ្នកឆាប់រហ័ស\n"
            "» @ADzAYTER\n"
            "» @LongzzSMMDIGItaLL")
    bot.send_message(message.chat.id, text)

# ចាប់ផ្ដើមដំណើរការ Bot
if __name__ == "__main__":
    print("Bot កំពុងដំណើរការ...")
    bot.infinity_polling()
