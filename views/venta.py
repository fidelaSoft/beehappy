import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from database.database import DataBase
class Venta:
    def __init__(self):
        self.lista_clientes = DataBase().get_clientes()
        self.lista_productos = DataBase().get_productos()

        self.root = Tk()
        self.root.geometry("600x400")
        self.root.title("Venta")


        self.titulo = tkinter.Label(text="Venta").grid(row=0, column=1)

        self.id_del_cliente_label = tkinter.Label(self.root, text="Id del cliente:").grid(row=1, column=0, sticky="w"                                                                                                       "")
        self.id_del_cliente_combo = ttk.Combobox(state="readonly", values=self.get_nombre_clientes()).grid(row=1, column=1, sticky="w")

        self.id_del_producto_label = tkinter.Label(self.root, text="Id del producto:").grid(row=2, column=0, sticky="w")
        self.id_del_producto_combo = ttk.Combobox(state="readonly", values=self.get_nombre_producto()).grid(row=2, column=1, sticky="w")

        self.cantidad_label = tkinter.Label(self.root, text="Cantidad:").grid(row=3, column=0, sticky="w")
        self.cantidad_entry = tkinter.Entry(self.root).grid(row=3, column=1)

        self.items = Treeview(self.root, column=("#1","#2","#3","#4"))
        self.items.column("#0",width=80)
        self.items.column("#1", width=80)
        self.items.column("#2", width=80)
        self.items.column("#3", width=80)
        self.items.column("#4", width=80)
        self.items.heading("#0", text="Id", anchor=CENTER)
        self.items.heading("#1", text="Producto", anchor=CENTER)
        self.items.heading("#2", text="Cantidad", anchor=CENTER)
        self.items.heading("#3", text="Precio", anchor=CENTER)
        self.items.heading("#4", text="Sub total", anchor=CENTER)
        self.items.grid(row=4,column=1)






        self.total_label = tkinter.Label(self.root, text="total").grid(row=6, column=0, sticky="w")
        self.total_entry = tkinter.Entry(self.root).grid(row=6, column=1)

        self.marco_acciones = tkinter.Frame(background="gray")
        self.marco_acciones.grid(row=7, column=1, pady=15)
        self.btn_emitir_factura = tkinter.Button(self.marco_acciones, text="Emitir factura", background="gray").grid(row=6, column=1)


        self.root.mainloop()

    def get_nombre_clientes(self):
        nombres = []
        for c in self.lista_clientes:
            nombres.append(c.nombre+" "+c.apellido)
        return nombres
    def get_nombre_producto(self):
        nombres = []
        for c in self.lista_productos:
            nombres.append(c.presentacion + " / " + c.descripcion)
        return nombres


fmr= Venta()

