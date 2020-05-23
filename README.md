# WKBL 알리미 Telegram Chatbot 
> 한국 여자프로농구 WKBL 순위 정보 알리미 Telegram Chatbot   
[챗봇 접속](t.me/wkblbot)
   
***유용하게 쓰셨다면 상단 star [![GitHub stars](https://img.shields.io/github/stars/ohahohah/github-tutorial.svg?style=social)](https://github.com/ohahohah/basketball-chatbot) 를 눌러주세요!***
  
## 주요 기능 Key Feature
- 한국 여자프로농구 WKBL 순위 정보를 Telegram chatbot으로 제공
- 순위 정보는 웹 스크래핑 사용

![run_chatbot](https://user-images.githubusercontent.com/64644871/82729455-a9bec980-9d32-11ea-9678-9bb847f0cba1.gif)
## chat bot 명령어 
- `/start` : 챗봇 시작       

## Project 구조
- [config 파일 예시](./config.json.example)
  - telegram token 등 공유되면 안되는 정보를 저장.
  - 사용할 때는 파일명을 `config.json` 으로 변경. git으로 공유되지 않음   
  ([.gitignore](./.gitignore)에 `config.json` 이 적혀있기 때문에 git이 파일을 tracking 하지 않음)
- [chatbot.py](./chatbot.py) : chatbot 프로그램  
- [scrap_ranking.py](./scrap_ranking.py) : 웹 스크래핑을 사용해 WKBL 순위를 가져옴
- [record.json](./record.json) : [웹 스크래핑 - scrap_ranking.py](./scrap_ranking.py)으로 가져온 정보를 저장한 파일  
_practice 폴더는 연습용_  

## Reference
- [Python telegram API- sample code(conversationbot)](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/conversationbot.py)
- [네이버 스포츠 - 여자 프로농구](https://sports.news.naver.com/basketball/record/index.nhn?category=wkbl)
- [웹 기초 참고자료 by ohahohah](https://www.notion.so/ohahohah/a0c5fd08a99744dd869f9322cc2f0972) 
- [github-tutorial by ohahohah](https://github.com/ohahohah/github-tutorial) : repository template으로 사용

## Links
- Project homepage: https://github.com/ohahohah/basketball-chatbot/
- Repository: https://github.com/ohahohah/basketball-chatbot/
  
## License
Jososo - [atccsy89@gmail.com](mailto:atcsy89@gmail.com)  
ohahohah – [ohahohah.dev@gmail.com](mailto:ohahohah.dev+gh@gmail.com)

MIT license를 준수합니다. [LICENSE](LICENSE)에서 자세한 정보를 확인할 수 있습니다.  
