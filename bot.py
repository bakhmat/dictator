from telegram.ext import Updater, CommandHandler, MessageHandler

def start(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text = 'Start')


def show_error(bot, update, error):
    print(error)

def main():
    updater = Updater('371335485:AAHRXayFZiMhDKvO1Bt3SiJAnFVAi45Nqp8Q')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))



    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()