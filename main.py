import telebot

# Buraya kendi bot token'ını yaz
TOKEN = "8208171283:AAF2JIftZ0efYjS855uYWWRZxXlAGYqaUJ8

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Merhaba! 🤖 Ben senin yapay zeka botunum!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Bunu söyledin: " + message.text)

print("Bot çalışıyor...")
bot.polling()
