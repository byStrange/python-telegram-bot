import telepot

bot = telepot.Bot('2009593665:AAHHtxHIBv288p_-u6lcTRBmI0IJNFYUEYo')
print(
    bot.getChat('1359290361')
)
bot.sendAudio(
    '1359290361', 'file:///C:/Users/stark/desktop/Music%202021/After%20Dark%20(TikTok%20aesthetics).mp3')
print('Audio send')
