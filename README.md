# bot-affiliati
Bot Telegram automatico per offerte Amazon
from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
BOT_TOKEN = os.environ.get("BOT_TOKEN")

CANALI = [
    "@affaritech_official",
    "@offerte_casa_italia",
    "@mangagaming_deals",
    "@super_offerte_italia_2025",
    "@svapo_offerte_italia"
]

MESSAGGIO_TEST = "🚀 Il bot è attivo e sta pubblicando H24 automaticamente nei canali! ✅"

def start(update: Update, context):
    update.message.reply_text("🤖 Bot attivo su Railway 24/7!")

def pubblica_tutti(update: Update, context):
    bot = context.bot
    for canale in CANALI:
        try:
            bot.send_message(chat_id=canale, text=MESSAGGIO_TEST)
            update.message.reply_text(f"✅ Inviato in {canale}")
        except Exception as e:
            update.message.reply_text(f"❌ Errore in {canale}: {e}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("pubblica_tutti", pubblica_tutti))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
