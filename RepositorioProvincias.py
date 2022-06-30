from typing import List
from Provincia import Provincia
from ManejadorProvincias import ManejadorProvincias
from ObjectEncoder import ObjectEncoder


class RepositorioProvincias:
    __conn = None
    __manejador = None

    def __init__(self, conn:ObjectEncoder) -> None:
        self.__conn = conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador = self.__conn.decodificarDiccionario(diccionario)
    

    def obtenerListaProvincias(self) -> List[Provincia]:
        return self.__manejador.getListaProvincias()


    def agregarProvincia(self, unaProvincia:Provincia) -> Provincia:
        self.__manejador.agregarProvincia(unaProvincia)
        return unaProvincia
    

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())