class Provincia:
    __nombre = None
    __capital = None
    __habitantes = None
    __departamentos = None

    def __init__(self, nombre:str, capital:str, habitantes:int, departamentos:int) -> None:
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena")
        if not isinstance(capital, str):
            raise TypeError("La capital debe ser una cadena")
        if not isinstance(habitantes, int):
            raise TypeError("El numero de habitantes debe ser un entero")
        if not isinstance(departamentos, int):
            raise TypeError("El numero de departamentos debe ser un entero")
        
        self.__nombre = nombre
        self.__capital = capital
        self.__habitantes = habitantes
        self.__departamentos = departamentos
    
    def getNombre(self) -> str:
        return self.__nombre
    
    def getCapital(self) -> str:
        return self.__capital
    
    def getHabitantes(self) -> int:
        return self.__habitantes
    
    def getDepartamentos(self) -> int:
        return self.__departamentos
    

    def toJSON(self) -> dict:
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre=self.__nombre,
                capital=self.__capital,
                habitantes=self.__habitantes,
                departamentos=self.__departamentos
            )
        )
        return d