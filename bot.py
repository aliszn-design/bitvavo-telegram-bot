import os
import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🚀 Your Trading Bot is Live")

def notify(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="📈 Example Buy Signal: Buy ETH/EUR at €3410")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('notify', notify))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
