from time import time
from VistaNuevaProvincia import VistaNuevaProvincia
from VistaPrincipal import VistaPrincipal
from RepositorioProvincias import RepositorioProvincias
from Tiempo import Tiempo


class ControladorProvincias:
    def __init__(self, repo:RepositorioProvincias, vista:VistaPrincipal) -> None:
        self.repo = repo
        self.vista = vista
        self.provincias = list(repo.obtenerListaProvincias())
    

    def crearProvincia(self):
        # Se crea una nueva provincia creando una instancia de la visa correspondiente
        nuevaProvincia = VistaNuevaProvincia(self.vista).show()
        # Se agrega la provincia al repositorio, la lista propia del controlador y a la vista
        if nuevaProvincia:
            unaProvincia = self.repo.agregarProvincia(nuevaProvincia)
            self.provincias.append(unaProvincia)
            self.vista.agregarProvincia(unaProvincia)
    

    def seleccionarProvincia(self, index):
        # Despliega una vista con la provincia seleccionada
        unaProvincia = self.provincias[index]
        tiempo = Tiempo(unaProvincia)
        self.vista.verProvinciaEnForm(unaProvincia, tiempo)
    

    def start(self):
        for p in self.provincias:
            self.vista.agregarProvincia(p)
        self.vista.mainloop()


    def salirGrabarDatos(self):
        self.repo.grabarDatos()