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

with open('ranking.json', 'r', encoding='UTF-8') as s:
    record = json.load(s)  # ranking.json 이라는 파일의 내용을 가져온다.


def proc_ranking(bot, update):
    # with open('ranking.json', 'r', encoding='UTF-8') as s:
    #     record = json.load(s)  # ranking.json 이라는 파일의 내용을 가져온다.
    print(record[0])
    # for key, value in ranking.items():
    #     # print(key, '위 ', value)
    msg = str(record[0])  # 이부분을 str로 받으니까 왜 되는거지?
    wkbl.sendMessage(msg)


def proc_winningrate(bot, update):
    msg = str(record[2])
    wkbl.sendMessage(msg)


def proc_win(bot, update):
    msg = str(record[3])
    wkbl.sendMessage(msg)


def proc_loose(bot, update):
    msg = str(record[4])
    wkbl.sendMessage(msg)


def proc_gap(bot, update):
    msg = str(record[5])
    wkbl.sendMessage(msg)


def proc_score(bot, update):
    msg = str(record[6])
    wkbl.sendMessage(msg)


def proc_stop(bot, update):
    wkbl.sendMessage('다음에 만나요.')
    wkbl.stop()


wkbl = chatbotmodel.Botwkbl()
wkbl.add_handler('ranking', proc_ranking)
wkbl.add_handler('winningrate', proc_winningrate)
wkbl.add_handler('win', proc_win)
wkbl.add_handler('loose', proc_loose)
wkbl.add_handler('gap', proc_gap)
wkbl.add_handler('score', proc_score)
wkbl.add_handler('stop', proc_stop)
wkbl.start()
