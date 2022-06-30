from cgitb import handler
import tkinter as tk

from Provincia import Provincia


class VistaListaProvincias(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.lb.configure(selectbackground="#0487D9")
    

    def insertar(self, unaProvincia:Provincia, index=tk.END):
        # Inserta el nombre de una provincia en la lista visible al usuario
        texto = "{}".format(unaProvincia.getNombre())
        self.lb.insert(index, texto)
    

    def bind_doble_click(self, callback):
        # Forma una funcion que llama a callback (posteriormente sera el metodo seleccionarProvincia del controlador)
        # pasando como parametro el indice de la provincia seleccionada
        handler = lambda _: callback(self.lb.curselection()[0])
        # Asocia la accion de dar doble click sobre una provincia con la funcion formada
        self.lb.bind("<Double-Button-1>", handler)