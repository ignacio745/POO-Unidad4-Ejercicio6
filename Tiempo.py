import json
import requests
from Provincia import Provincia


class Tiempo:
    """
    Esta es una clase utilizada para obtener el tiempo de una provincia
    """
    __temperatura = None
    __sensacionTermica = None
    __humedad = None

    def __init__(self, unaProvincia:Provincia) -> None:
        aux = json.loads(requests.get("http://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=b270c8fc015a2cf595e48696fa1d5b35".format(unaProvincia.getCapital())).content)
        self.__temperatura = aux["main"]["temp"]
        self.__sensacionTermica = aux["main"]["feels_like"]
        self.__humedad = aux["main"]["humidity"]
        pass
    

    def getTemperatura(self):
        return self.__temperatura
    
    def getSensacionTermica(self):
        return self.__sensacionTermica
    
    def getHumedad(self):
        return self.__humedad