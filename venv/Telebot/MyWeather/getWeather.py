from pyowm import OWM


def Weath(city):
    owm = OWM('00eda13e5a9af69a1d143757112a3c28')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    print(w.status)
    return w