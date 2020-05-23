import telegram
from telegram.ext import Updater, CommandHandler
import json

with open('../../config.json', 'r') as f:
    config = json.load(f)  # config.json 이라는 파일의 내용을 가져온다.


class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token, use_context=True)
        self.id = config['TEST_ID']
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id=self.id, text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()


class Botwkbl(TelegramBot):
    def __init__(self):
        secret_key = config['TELEGRAM_TOKEN']  # Telegram Token 값을 scret_key라는 변수에 담는다
        self.token = secret_key
        TelegramBot.__init__(self, 'wkbl', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('안녕하세요. 무엇을 알고 싶으세요?'
                         '\n/ranking \n/winningrate \n/win \n/loose \n/gap \n/score \n/stop')
        self.updater.start_polling()
        self.updater.idle()
