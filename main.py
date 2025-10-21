import telebot

# Telegram bot tokenını buraya yaz:
TOKEN = "8208171283:AAF2JIftZ0efYjS855uYWWRZxXlAGYqaUJ8"  # <-- tırnaklar içinde!

import logging
import asyncio
import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# === YAPAY ZEKA BEYNİ ===
openai.api_key = os.getenv("OPENAI_API_KEY")  # Render'da Environment'a ekle

# === OTOMATİK HATA YÖNETİMİ ===
class AutoFixBrain:
    def __init__(self):
        self.error_log = []

    async def handle_error(self, error):
        self.error_log.append(str(error))
        print(f"[⚠️ HATA ALGILANDI] {error}")
        if "Timed out" in str(error):
            print("[⏱️] Zaman aşımı → yeniden bağlanılıyor...")
        elif "Unauthorized" in str(error):
            print("[🔐] Token hatası → lütfen yeni token girin.")
        elif "NetworkError" in str(error):
            print("[🌐] Ağ hatası → tekrar bağlanılıyor...")
        else:
            print("[🤖] Tanımsız hata kaydedildi.")

bot_brain = AutoFixBrain()

# === TELEGRAM TOKENİNİ BURAYA YAZ ===
TOKEN = "BURAYA_TELEGRAM_TOKENİNİ_YAZ"

# === KOMUTLAR ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Meshurx beyin aktif! Ne konuşmak istersin?")

# === MESAJI ALIP OPENAI'YE GÖNDERME ===
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.message.from_user.first_name
    print(f"[📩] {user_id}: {user_text}")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen Meshurx adlı yardımcı bir yapay zekasın. Kibar, yaratıcı ve hızlısın."},
                {"role": "user", "content": user_text}
            ]
        )
        reply = response.choices[0].message["content"]
        await update.message.reply_text(reply)
    except Exception as e:
        await bot_brain.handle_error(e)
        await update.message.reply_text("⚠️ Şu anda yanıt veremiyorum, birazdan tekrar dene.")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    await bot_brain.handle_error(context.error)

# === ANA FONKSİYON ===
async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error_handler)

    print("🚀 Meshurx AI Bot + Beyin yüklendi.")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
