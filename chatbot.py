#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import json

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

with open('record.json', 'r', encoding='utf-8') as record_file:
    record = json.load(record_file)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

RANKING = range(1)


def start(update, context):
    reply_keyboard = [['RANKING']]

    update.message.reply_text(
        '안녕하세요. 순위를 알려드릴게요'
        '그만하고 싶으시면 /cancel 을 눌러주세요.\n\n',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return RANKING


def show_ranking(update, context):
    ranking = record[0]
    msg = ''

    for key, value in ranking.items():
        str = key + '위' + value + '\n'
        msg += str
    update.message.reply_text(msg)

    update.message.reply_text('안녕히 가세요. 다시 시작하려면  /start 를 써주세요',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('안녕히 가세요. 다음에 만나요.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Telegram bot token 불러오기
    token = config['TELEGRAM_TOKEN']  # Telegram Token 값을 scret_key라는 변수에 담는다
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            RANKING: [MessageHandler(Filters.regex('^(RANKING)$'), show_ranking)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    updater.idle()


if __name__ == '__main__':
    main()
