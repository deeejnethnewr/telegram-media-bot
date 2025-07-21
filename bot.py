import os
import subprocess
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Send me a YouTube playlist, Drive or Dailymotion link!")

def handle_message(update: Update, context: CallbackContext):
    url = update.message.text.strip()
    update.message.reply_text("Downloading...")
    subprocess.run(["yt-dlp", url])
    for file in os.listdir():
        if file.endswith((".mp4", ".mkv", ".webm", ".mp3")):
            update.message.reply_document(open(file, 'rb'))

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
