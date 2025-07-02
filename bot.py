import os
import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

CANALI = [
    "@affaritech_official",
    "@offerte_casa_italia",
    "@mangagaming_deals",
    "@super_offerte_italia_2025",
    "@svapo_offerte_italia"
]

MESSAGGIO_TEST = "🚀 Il bot è attivo e pronto a pubblicare offerte automatiche!"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🤖 Bot attivo su Railway 24/7!")

def pubblica_tutti(update: Update, context: CallbackContext):
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
    dp.add_handler(CommandHandler("pubblica", pubblica_tutti))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
