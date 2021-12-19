import telepot
from pprint import pprint

API_TOKEN = '5084415268:AAF07r-9pYvTtQJZ086BOr2r5iZxb8dG5q4 '
bot = telepot.Bot(API_TOKEN)
re = bot.getUpdates()
pprint(re)
