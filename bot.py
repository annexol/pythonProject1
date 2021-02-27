import telebot
import requests
from bs4 import BeautifulSoup
from lxml import html
from telebot import types





url1 = 'https://afisha.tut.by/concert/'
url2 = 'https://afisha.tut.by/theatre/'
url3 = 'https://afisha.tut.by/film/'
url4 = 'https://afisha.tut.by/party/'
url5 = 'https://afisha.tut.by/other/'
url6='https://afisha.tut.by/free-events/'
day_type=0
to_url=0

bot = telebot.TeleBot('1643809445:AAE90eHD2vIPwFZPjj0CnYCqmtqjPyFo6GI')

keyboard_day = types.InlineKeyboardMarkup()
i_today = types.InlineKeyboardButton(text='Сегодня', callback_data='today')
i_tomorrow = types.InlineKeyboardButton(text='Завтра', callback_data='tomorrow')
i_day_after_tomorrow = types.InlineKeyboardButton(text='Послезавтра', callback_data='aftomorrow')
keyboard_day.add(i_today, i_tomorrow, i_day_after_tomorrow)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, text='*'*47+' '+'ЗДЕСЬ МОГЛА БЫТЬ ВАША РЕКЛАМА))))))'+' '+'*'*47)
    keyboard_event = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i_concert = types.KeyboardButton(text='Концерт')
    i_theatre = types.KeyboardButton(text='Театр')
    #i_film = types.KeyboardButton(text='Кинотеатр')
    i_party = types.KeyboardButton(text='Вечеринка')
    i_other = types.KeyboardButton(text='Другое')
    i_no_cash = types.KeyboardButton(text='Бесплатно')
    keyboard_event.add(i_concert, i_party, i_theatre, i_other, i_no_cash)
    bot.send_message(message.chat.id,text='Здравствуйте, выберете мероприятие', reply_markup=keyboard_event)


@bot.message_handler(content_types='text')
def time(type):
    global to_url
    if type.text=="Концерт":
        day(type)
        to_url = 1

    elif type.text == "Театр":
        day(type)
        to_url = 2

    elif type.text == "Кинотеатр":
        day(type)
        to_url = 3

    elif type.text == "Вечеринка":
        day(type)
        to_url = 4

    elif type.text == "Другое":
        day(type)
        to_url = 5

    elif type.text == "Бесплатно":
        day(type)
        to_url = 6


def day(type):
    bot.reply_to(type, text='Когда желаете пойти?', reply_markup=keyboard_day)

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    global day_type
    global to_url
    if call.data == 'today':
        day_type = 1
        if to_url==1:
            bot.send_message(call.from_user.id, text=main(url1), reply_markup=keyboard_day)
        elif to_url==2:
            bot.send_message(call.from_user.id, text=main(url2), reply_markup=keyboard_day)
        elif to_url==3:
            bot.send_message(call.from_user.id, text=main(url3), reply_markup=keyboard_day)
        elif to_url == 4:
            bot.send_message(call.from_user.id, text=main(url4), reply_markup=keyboard_day)
        elif to_url==5:
            bot.send_message(call.from_user.id, text=main(url5), reply_markup=keyboard_day)
        elif to_url==6:
            bot.send_message(call.from_user.id, text=main(url6), reply_markup=keyboard_day)

    elif call.data == 'tomorrow':
        day_type = 2
        if to_url==1:
            bot.send_message(call.from_user.id, text=main(url1), reply_markup=keyboard_day)
        elif to_url==2:
            bot.send_message(call.from_user.id, text=main(url2), reply_markup=keyboard_day)
        elif to_url==3:
            bot.send_message(call.from_user.id, text=main(url3), reply_markup=keyboard_day)
        elif to_url == 4:
            bot.send_message(call.from_user.id, text=main(url4), reply_markup=keyboard_day)
        elif to_url==5:
            bot.send_message(call.from_user.id, text=main(url5), reply_markup=keyboard_day)
        elif to_url==6:
            bot.send_message(call.from_user.id, text=main(url6), reply_markup=keyboard_day)

    elif call.data == 'aftomorrow':
        day_type = 3
        if to_url==1:
            bot.send_message(call.from_user.id, text=main(url1), reply_markup=keyboard_day)
        elif to_url==2:
            bot.send_message(call.from_user.id, text=main(url2), reply_markup=keyboard_day)
        elif to_url==3:
            bot.send_message(call.from_user.id, text=main(url3), reply_markup=keyboard_day)
        elif to_url == 4:
            bot.send_message(call.from_user.id, text=main(url4), reply_markup=keyboard_day)
        elif to_url==5:
            bot.send_message(call.from_user.id, text=main(url5), reply_markup=keyboard_day)
        elif to_url==6:
            bot.send_message(call.from_user.id, text=main(url6), reply_markup=keyboard_day)


def get_htmlurl(url):
    urls=url
    return urls

def get_html(url):
    urls=url
    r = requests.get(url)
    return r.text


def get_data(html, urls):
    urlss=urls
    soup = BeautifulSoup(html, 'lxml')
    #h1 = soup.find('div', class_="event-header-i").find('a').text
    #h2 = soup.find('div', class_="item-header-i").find('a').text
    #h3 = soup.find('div', class_="event-session js-session-list-wrapper").find('a').text
    #h4= soup.find('div', class_="event-header-i").find('a').get('href')
    lis = []
    h1 = soup.find('div', class_='b-afisha-events js-ttinfo concert-events')
    for i in h1:
        lis.append(i)
    l = str(lis[1])
    x = l.split('b-afisha-event-title')
    today1 = x[1].split('div ')
    today_amount1 = 0
    for t in today1:
        if t == 'class="b-afisha-event js-film-info">\n<':
            today_amount1 += 1
    today2 = x[2].split('div ')
    today_amount2 = 0
    for t in today2:
        if t == 'class="b-afisha-event js-film-info">\n<':
            today_amount2 += 1
    today_amount2=today_amount2+today_amount1
    today3 = x[3].split('div ')
    today_amount3 = 0
    for t in today3:
        if t == 'class="b-afisha-event js-film-info">\n<':
            today_amount3 += 1
    today_amount3=today_amount3+today_amount2



    if day_type==1:
        return a(y1=0,y=today_amount1,urlss=urlss)
    elif day_type==2:
        return a(y1=today_amount1,y=today_amount2,urlss=urlss)
    elif day_type==3:
        return a(y1=today_amount2,y=today_amount3,urlss=urlss)




def a(y1,y,urlss):
    x=y-y1
    url=urlss
    p = get_html(url)
    tree = html.fromstring(p)
    list_place=[]
    list_name=[]
    list_hrev=[]
    list_time=[]
    place = (tree.xpath("//div[@class='b-afisha-event js-film-info']/div[@class='a-event-i' and 1]/div[@class='a-event-header ' and 1]/div[@class='event-header-i' and 1]/a[@class='header__link' and 1]"))
    name = (tree.xpath("//a[@class='header__link']/span[1]"))
    href= (tree.xpath("//div[@class='b-afisha-event js-film-info']/div[@class='a-event-i' and 1]/div[@class='a-event-list js-film-list-wrapper' and 2]/div[@class='event-list-i' and 1]/div[@class='a-event-item js-film-list' and 1]/div[@class='event-item-i js-film-list__li' and 1]/div[@class='item-header' and 1]/div[@class='item-header-i' and 1]/a[@class='header__link' and 1]"))
    time = (tree.xpath("//div[@class='b-afisha-event js-film-info']/div[@class='a-event-i' and 1]/div[@class='a-event-list js-film-list-wrapper' and 2]/div[@class='event-list-i' and 1]/div[@class='a-event-item js-film-list' and 1]/div[@class='event-item-i js-film-list__li' and 1]/div[@class='event-session js-session-list-wrapper' and 2]/div[@class='event-session-i js-session-list' and 1]/ul[@class='b-shedule__list js-shedule-list' and 1]/li[@class='shedule__li' and 1]/a[@class='tooltip-holder event-time past' and 1]"))

    for i in place[y1:y]:
        list_place.append(i.text)
    for i in name[y1:y]:
        list_name.append(i.text)
    for i in href[y1:y]:
        list_hrev.append(i.get('href'))
    for i in time [y1:y]:
        list_time.append(i.text)

    ab=''
    for i in range(0,x):
        ab+=((str(i+1)+')'+' '+str(list_name[i])+' '+str(list_hrev[i]+' '+'-'+' '+str(list_place[i])+'\n'+'\n')))
    return ab








def main(url):
    return (get_data(get_html(url),get_htmlurl(url)))



#print (main(url1))
bot.polling()