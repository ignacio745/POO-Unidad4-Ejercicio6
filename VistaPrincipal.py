from struct import pack
import tkinter as tk
from VistaProvinciaDetalladaForm import VistaProvinciaDetalladaForm
from VistaListaProvincias import VistaListaProvincias

class VistaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Lista de provincias")
        self.list = VistaListaProvincias(self, height=15)
        self.form = VistaProvinciaDetalladaForm(self)
        self.btn_new = tk.Button(self, text="Agregar provincia")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
    

    def setControlador(self, ctrl):
        # Asocia los metodos correspondientes del controlador a los metodos de las vistas que lo requieran
        self.btn_new.config(command=ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.seleccionarProvincia)
    

    def agregarProvincia(self, unaProvincia):
        # Agrega una provincia a la lista visible al usuario
        self.list.insertar(unaProvincia)
    

    def verProvinciaEnForm(self, unaProvincia, tiempo):
        # Se muestra la provincia nueva con sus datos en el formulario de la ventana principal
        self.form.mostrarEstadoProvinciaEnFormulario(unaProvincia, tiempo)