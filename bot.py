#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'эй'
    print(text)
    update.message.reply_text(text)
    # №update.message.reply_text(update.message.from_user.first_name + ' ' + update.message.from_user.last_name)
     # print('start has been executed')
    # print('Your name is ' + update.message.from_user.first_name + ' ' + update.message.from_user.last_name)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    # logging.basicConfig(level=logging.DEBUG)
    updater = Updater("505229871:AAFy8VCt_-gIHHex_X-b6UjfIotAeloRNI4")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()
# Вызываем функцию - эта строчка собственно запускает бота
main()