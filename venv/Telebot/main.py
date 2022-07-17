import MyWeather.getWeather
import Telebot.Scr.Script

import telebot
import Telebot.Token.Token
TokenTG = Telebot.Token.Token.TokenTelegram

bot = telebot.TeleBot(token=TokenTG)


@bot.message_handler(commands=['Start'])
def Cmd(message):
   bot.send_message(message.chat.id, "Введите название населенного пункта")
@bot.message_handler(content_types=['text'])
def WeatherBot(message):
    city = message.text
    print(city)
    try:
        ww = MyWeather.getWeather.Weath(city)
        bot.send_message(message.chat.id, f"Температура в {city}  "
                                         f"{str(int(ww.temperature('celsius')['temp']))} градусов")
        bot.send_message(message.chat.id, f"Погода в {city} {Telebot.Scr.Script.Status(ww.status)} ", parse_mode='html')
    except:
        bot.send_message(message.chat.id, "Такого города не существует")
        print("Такого города не существует")


print("Start Bot")

bot.polling(none_stop=True)
