from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler
import handlers


def main(token):
    # updater
    updater = Updater(token)

    # dispatcher
    dispatcher = updater.dispatcher

    # command handlers
    dispatcher.add_handler(CommandHandler('start', handlers.start))

    # message handlers
    dispatcher.add_handler(MessageHandler(Filters.text('Valyuta'), handlers.valyuta))
    dispatcher.add_handler(MessageHandler(Filters.text('Hisoblash'), handlers.hisoblash))
    dispatcher.add_handler(MessageHandler(Filters.text, handlers.hisobla))
    # dispatcher.add_handler(CallbackQueryHandler(handlers.hisoblash,pattern="hisoblash"))
    dispatcher.add_handler(MessageHandler(Filters.text('📝 About'), handlers.about))

    # start polling
    updater.start_polling()
    updater.idle()