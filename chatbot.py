import telegram
import sys
import chatbotmodel
import json

with open('config.json', 'r') as f:
    config = json.load(f)  # config.json 이라는 파일의 내용을 가져온다.

secret_key = config['TELEGRAM_TOKEN']  # Telegram Token 값을 scret_key라는 변수에 담는다
wkbl_token = secret_key

wkblchatbot = telegram.Bot(token=wkbl_token)
updates = wkblchatbot.getUpdates()

for u in updates:
    print(u.message)


def proc_ranking(bot, update):
    with open('ranking.json', 'r', encoding='UTF-8') as s:
        ranking = json.load(s)  # ranking.json 이라는 파일의 내용을 가져온다.

    for key, value in ranking.items():
        # print(key, '위 ', value)
        msg = key + '위 ' + value
        wkbl.sendMessage(msg)


def proc_stop(bot, update):
    wkbl.sendMessage('다음에 만나요.')
    wkbl.stop()


wkbl = chatbotmodel.Botwkbl()
wkbl.add_handler('ranking', proc_ranking)
wkbl.add_handler('stop', proc_stop)
wkbl.start()
