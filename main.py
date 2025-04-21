from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello! I am your Aviator Predictor Bot.')

def main():
    updater = Updater("7520521128:AAFknHDIUW7D-XdwCzy0SiRyZRjoh1XNk3Y", use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello! I am your Aviator Predictor Bot.')

def main():
    token = os.getenv("BOT_TOKEN")
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello! I am your Aviator Predictor Bot.')

def main():
    token = os.getenv("BOT_TOKEN")
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello! I am your Aviator Predictor Bot.')

def main():
    updater = Updater("7520521128:AAFknHDIUW7D-XdwCzy0SiRyZRjoh1XNk3Y", use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def predict(update: Update, context: CallbackContext):
    update.message.reply_text('Predicting... stay tuned!')

dispatcher.add_handler(CommandHandler("predict", predict))
