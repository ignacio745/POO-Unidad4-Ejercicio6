from Provincia import Provincia
from VistaProvinciaForm import VistaProvinciaForm

import tkinter as tk

class VistaNuevaProvincia(tk.Toplevel):
    """
    Ventana que se despliega para solicitar los datos de una nueva provincia
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.provincia = None
        self.form = VistaProvinciaForm(self) 
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)
    
    

    def confirmar(self):
        # Es el comando que se le asocia al boton "Confirmar"
        # Consiste en asignar al atributo provincia la provincia resultanta del metodo crearProvinciaDesdeFormulario y destruir la ventana
        self.provincia = self.form.crearProvinciaDesdeFormulario()
        if self.provincia:
            self.destroy()
        
    
    def show(self) -> Provincia:
        # Es el metodo que se invoca en el controlador inmediatamente despues de crear una instancia de esta clase
        # Consiste en 
        # Evitar que el usuario pueda interactuar con la ventana principal antes de cerrar esta
        self.grab_set()
        # Esperar a que la ventana sea cerrada para retornar el atributo almacenado en provincia
        # Ya que, como se establece en el metodo confirmar, la formacion de la provincia esta estrechamente ligada al cierre de la ventana
        # Puede comprobarse que es necesario estableciendo un breakpoint en este punto
        self.wait_window()
        # Retorna lo contenido dentro del atributo provincia, que ahora es una provincia, 
        # suponiendo que se cerro la ventana a traves del boton "Confirmar"
        return self.provincia