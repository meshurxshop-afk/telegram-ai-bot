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
import logging
import time
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import TelegramError, NetworkError

# --- BEYİN BAŞLANGICI ---
class AutoFixBrain:
    def __init__(self):
        self.error_log = []

    def log_error(self, error):
        print(f"[⚠️ HATA ALGILANDI] {error}")
        self.error_log.append(str(error))

    def fix_error(self, error):
        if "NetworkError" in str(error):
            print("[🔁] Ağ hatası algılandı → yeniden bağlanılıyor...")
            time.sleep(3)
            return "retry"
        elif "Unauthorized" in str(error):
            print("[🔐] Token geçersiz → lütfen yeni token girin.")
            return "alert"
        elif "Timed out" in str(error):
            print("[⏱️] Zaman aşımı → tekrar deneniyor...")
            return "retry"
        else:
            print("[🤖] Tanımsız hata → kayıt altına alındı.")
            return "log"
# --- BEYİN SONU ---

# Telegram BOT AYARLARI
TOKEN = "8208171283:AAF2JIftZ0efYjS855uYWWRZxXlAGYqaUJ8"
bot_brain = AutoFixBrain()

def start(update, context):
    update.message.reply_text("🧠 Akıllı sistem aktif! Hoş geldin kral 👑")

def handle_message(update, context):
    text = update.message.text.lower()
    update.message.reply_text(f"🤖 Cevap: {text.capitalize()} (AI sistemi aktif)")

def error_handler(update, context):
    error = context.error
    bot_brain.log_error(error)
    action = bot_brain.fix
