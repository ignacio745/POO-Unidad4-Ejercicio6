from typing import List
from Provincia import Provincia

class ManejadorProvincias:
    __provincias = None
    __indice = None

    def __init__(self) -> None:
        self.__provincias:List[Provincia] = []
    

    def agregarProvincia(self, unaProvincia:Provincia) -> None:
        if not isinstance(unaProvincia, Provincia):
            raise TypeError("Solo pueden agregarse provincias")
        self.__provincias.append(unaProvincia)
    
    
    def getListaProvincias(self) -> List[Provincia]:
        return self.__provincias
    

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            provincias=[unaProvincia.toJSON() for unaProvincia in self.__provincias]
        )
        return d