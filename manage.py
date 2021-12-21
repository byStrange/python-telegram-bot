import schedule
from translate import Translator
from telepot import Bot
import requests
import json
import time
API_TOKEN = '5084415268:AAF07r-9pYvTtQJZ086BOr2r5iZxb8dG5q4'
group = -1001740928544
bot = Bot(API_TOKEN)


def translate(text, lang='uz'):
    translator = Translator(to_lang=lang)
    return translator.translate(text)


def getJoke():
    page = requests.get('https://v2.jokeapi.dev/joke/Any')
    text = json.loads(page.text)
    if 'joke' in text:
        return text['joke']
    else:
        return text['setup']


def postJoke():
    joke = getJoke()
    # res = f'JOKE\n\nEng:\n{joke}\nUz:\n{translate(joke)}'
    res = f'JOKE:\n{joke}'
    return res


def getFact():
    fact = requests.get('https://uselessfacts.jsph.pl/random.json')
    text = json.loads(fact.text)
    return text


def postFact():
    fact = getFact()
    t = fact['text']
    trans = translate(t, fact['language'])
    # res = f'Fact\n\nEng:{t}\nUz:{trans}'
    res = f'Fact:\n{t}'
    return res


def postMessageJoke():
    bot.sendMessage(group, postJoke())


def postMessageFact():
    bot.sendMessage(group, postFact())


schedule.every(1).minutes.do(postMessageFact)
schedule.every(1).minutes.do(postMessageJoke)

while 1:
    schedule.run_pending()
    time.sleep(1)

