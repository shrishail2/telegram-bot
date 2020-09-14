!pip install adafruit-io

x = "shrishailhiremath" #ADAFRUIT_IO_USERNAME
y = "aio_EFMV36bA7yTnsVCp08iZdpARRj5l" #ADAFRUIT_IO_KEY
from Adafruit_IO import Client, Feed
aio = Client(x,y)

#create a new feed
new = Feed(name='telegrambot2') #feed name is given
result = aio.create_feed(new)
result
from Adafruit_IO import Data
#sending a value to afeed
value =Data(value=0)
value_send = aio.create_data('telegrambot2',value)

!pip install python-telegram-bot

from telegram.ext import Updater,CommandHandler
import requests  # Getting the data from the cloud

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def on(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'light turned on'
    pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Green_sphere.svg/1024px-Green_sphere.svg.png'
    bot.send_message(chat_id,txt)
    bot.send_photo(chat_id,pic)
    from Adafruit_IO import Data
    value = Data(value=1)
    value_send = aio.create_data('telegrambot2',value)
 
def off(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'light is turning off'
    pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTuueKIndqjMG0rlzPZrO0UUFP6ts8b_CrUIQ&usqp=CAU'
    bot.send_message(chat_id,txt)
    bot.send_photo(chat_id,pic)
    value = Data(value=0)
    value_send = aio.create_data('telegrambot2',value)

u = Updater('1304573162:AAHP-32tgIzwv1cl754r06diyxeq0fTOdEM')  #change the token
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle() 
