import pandas
from GoogleNews import GoogleNews
from telepot import Bot
import schedule
import time
API_TOKEN = '5084415268:AAF07r-9pYvTtQJZ086BOr2r5iZxb8dG5q4'
GROUP_ID = -1001740928544
bot = Bot(API_TOKEN)
print('Bot started...')

news_result = ''


def get_news():
    news = GoogleNews(period="1d")
    news.search('uzbekistan')
    news_result = news.result()
# data = pandas.DataFrame.from_dict(news_result)
# data = data.drop(columns=['img'])
# data.head()


def pack_message(title, date, datetime, description, link, img=None):
    res = f"{title}  {date}\n{description}\nRead more:  {link}"
    post_message(res)


def post_message(text):
    bot.sendMessage(GROUP_ID, text)


i = 0


def post_data():
    global i
    pack_message(
        news_result[i]['title'],
        news_result[i]['date'],
        news_result[i]['desc'],
        news_result[i]['link'],
        news_result[i]['img'],
    )
    i += 1
    if i > len(news_result):
        get_news()
    # pack_message(
    #     i['title'],
    #     i['date'],
    #     i['datetime'],
    #     i['desc'],
    #     i['link'],
    #     i['img']
    # )


schedule.every(1).minutes.do(post_data)

while 1:
    schedule.run_pending()
