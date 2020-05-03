import telegram
import sys
import chatbotmodel
import json

with open('config.json', 'r') as f:
    config = json.load(f)  # config.json 이라는 파일의 내용을 가져온다.

secret_key = config['TELEGRAM_TOKEN']  # Telegram Token 값을 scret_key라는 변수에 담는다

wkbltest_token = secret_key
wkbltest = telegram.Bot(token=wkbltest_token)
updates = wkbltest.getUpdates()
for u in updates:
    print(u.message)


def proc_ranking(bot, update):
    wkbl_test.sendMessage('1위 우리은행')
    wkbl_test.sendMessage('2위 KB스타즈')
    wkbl_test.sendMessage('3위 하나은행')
    wkbl_test.sendMessage('4위 신한은행')
    wkbl_test.sendMessage('5위 BNK')
    wkbl_test.sendMessage('6위 삼섬생명')


def proc_stop(bot, update):
    wkbl_test.sendMessage('다음에 만나요.')
    wkbl_test.stop()


wkbl_test = chatbotmodel.Botwkbl_test()
wkbl_test.add_handler('ranking', proc_ranking)
wkbl_test.add_handler('stop', proc_stop)
wkbl_test.start()
