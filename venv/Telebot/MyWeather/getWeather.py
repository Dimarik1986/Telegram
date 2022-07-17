from pyowm import OWM
import Telebot.Token.Token

TokenOWM = Telebot.Token.Token.TokenWeather

def Weath(city):
    owm = OWM(TokenOWM)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    print(w.status)
    return w