import tkinter as tk
from tkinter import messagebox
from Provincia import Provincia

class VistaProvinciaForm(tk.LabelFrame):
    _fields = ("Nombre", "Capital", "Cantidad de habitantes", "Cantidad de departamentos/partidos")
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        # map hace que el metodo crearCampo se ejecute con cada uno de los campos self._fields
        self.entries = list(map(self.crearCampo, enumerate(self._fields)))
        self.frame.pack()

    

    def crearCampo(self, field) -> tk.Entry:
        # Crea un campo dada su posicion (fila) y su texto asociado
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=40)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry
    

    # Crea una provincia con los datos ingresados
    def crearProvinciaDesdeFormulario(self) -> Provincia:
        # Crea un objeto unaProvincia con None para siempre retornar algo
        unaProvincia = None
        # Crea una lista con los valores ingresados
        values = [e.get() for e in self.entries]
        try:
            # Intenta convertir los datos de las posiciones 2 y 3 a enteros, ya que son el numero de habitantes y de departamentos
            values[2] = int(values[2])
            values[3] = int(values[3])
        except:
            pass
        try:
            # Intenta crear la provincia
            unaProvincia = Provincia(*values)
        except TypeError as e:
            # En caso de fallar muestra un mensaje de error
            messagebox.showerror("Error de tipo", str(e), parent=self)
        
        # Retorna la provincia formada o un None en caso de no haber podido crearla
        return unaProvincia
    

    def limpiar(self):
        # Limpia todas las entradas
        for entry in self.entries:
            entry.delete(0, tk.END)