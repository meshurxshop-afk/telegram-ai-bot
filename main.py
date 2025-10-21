import telebot

# Telegram bot tokenını buraya yaz:
TOKEN = "8208171283:AAF2JIftZ0efYjS855uYWWRZxXlAGYqaUJ8"  # <-- tırnaklar içinde!

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Merhaba! 🤖 Ben Meshurx botum. Nasıl yardımcı olabilirim?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Aldım 👌: {message.text}")

print("✅ Bot aktif!")

bot.infinity_polling()
