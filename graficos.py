import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
from tkinter import scrolledtext as st
import ordenes_sql


class App:

    def __init__(self):
        self.bd = ordenes_sql.Comandos_sql()
        self.root = tk.Tk()
        self.root.title("Mantenimiento Base de datos")
        self.root.tk_setPalette("lightgrey")
        

        self.cuaderno1 = ttk.Notebook(self.root)
        self.cuaderno1.grid(column=0, row=0, padx= 10, pady=10, sticky="nsew")
        self.cargar()
        self.consulta()
        self.eliminar()
        self.modificar()
        self.listado_completo()
        
        self.root.mainloop()


    def cargar(self):
        self.carga_pagina1 = tk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.carga_pagina1, text="Cargar articulos")

        #labelframe
        self.carga_frame = ttk.LabelFrame(self.carga_pagina1, text="Cargar")
        self.carga_frame.pack(padx=10, pady=10)

        # labels
        self.carga_descripcion = ttk.Label(self.carga_frame, text="Descripcion")
        self.carga_descripcion.grid(column=0, row=1, padx=5,pady=5)
        self.carga_precio = ttk.Label(self.carga_frame, text="Precio")
        self.carga_precio.grid(column=0, row=2, padx=5,pady=5)

        # Entry         
        self.var_entry2 = tk.StringVar()
        self.carga_entry2 = ttk.Entry(self.carga_frame, width=20, textvariable=self.var_entry2)
        self.carga_entry2.grid(column=1,row=1, padx=5, pady=10)

        self.var_entry3 = tk.DoubleVar()
        self.carga_entry3 = ttk.Entry(self.carga_frame, width=20, textvariable=self.var_entry3)
        self.carga_entry3.grid(column=1,row=2, padx=5, pady=10)

        #button
        self.carga_button = ttk.Button(self.carga_frame, text="Guardar", command=self.cargar_sql)
        self.carga_button.grid(column=1, row=3, padx=10, pady=10)


    def cargar_sql(self):    
        datos=(self.var_entry2.get(), self.var_entry3.get())
        self.cargar_bd = self.bd.carga(datos)

        #mensajes
        ms.showinfo("Información", f"Los productos fueron ingresados correctamente \n con el codigo de producto {self.cargar_bd}")
        
        #dejamos en blanco las stringVar
        self.var_entry2.set("")
        self.var_entry3.set("")


    def consulta(self):
        self.consulta_pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.consulta_pagina2, text="Consultar")

        #labelFrame
        self.consultar_frame = ttk.LabelFrame(self.consulta_pagina2, text="Consultar")
        self.consultar_frame.pack(padx=10, pady=10)

        # labels 
        self.consulta_codigo = ttk.Label(self.consultar_frame, text="Codigo")
        self.consulta_codigo.grid(column=0, row=0, padx=5, pady=5)
        self.consulta_descripcion = ttk.Label(self.consultar_frame, text="Descripcion")
        self.consulta_descripcion.grid(column=0, row=1, padx=5, pady=5)
        self.consulta_precio = ttk.Label(self.consultar_frame, text="Precio")
        self.consulta_precio.grid(column=0, row=2, padx=5, pady=5)
        
        # Entry
        self.consulta_v_codigo1 = tk.StringVar()
        self.consulta_entry1 = ttk.Entry(self.consultar_frame,width=20, textvariable=self.consulta_v_codigo1)
        self.consulta_entry1.grid(column=1,row=0, padx=5, pady=10)
        
        self.consulta_v_codigo2 = tk.StringVar()
        self.consulta_entry2 = ttk.Entry(self.consultar_frame,width=20, textvariable=self.consulta_v_codigo2, state="readonly")
        self.consulta_entry2.grid(column=1,row=1, padx=5, pady=10)
        
        self.consulta_v_codigo3 = tk.StringVar()
        self.consulta_entry3 = ttk.Entry(self.consultar_frame,width=20, textvariable=self.consulta_v_codigo3, state="readonly")
        self.consulta_entry3.grid(column=1,row=2, padx=5, pady=10)

        #button
        self.consulta_button = ttk.Button(self.consultar_frame, text="Buscar", command=self.consulta_sql)
        self.consulta_button.grid(column=1, row=3, padx=10, pady=10)


    def consulta_sql(self):
        datos = self.consulta_v_codigo1.get()
        self.respuesta_bd = self.bd.consulta(datos)

        if self.respuesta_bd==[]:   #otra forma para comprobar es if len(self.respuesta_bd)>0: funciona de la misma manera
            ms.showerror("Error","El codigo ingresado no corresponde a ningún producto")
        else:
        #asignación de datos
            self.consulta_v_codigo2.set(self.respuesta_bd[0][0])
            self.consulta_v_codigo3.set(self.respuesta_bd[0][1])


    def eliminar(self):
        self.eliminar_pagina3  = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.eliminar_pagina3, text="Eliminar") 

        #labelFrame
        self.eliminar_frame = ttk.LabelFrame(self.eliminar_pagina3, text="Eliminar")
        self.eliminar_frame.pack(padx=10, pady=10)

        # labels
        self.eliminar_titulo = ttk.Label(self.eliminar_frame, text='"Ingrese el codigo del producto a eliminar"')
        self.eliminar_titulo.grid(column=0, row=0, padx=5, pady=5, columnspan=2)
        self.eliminar_descripcion = ttk.Label(self.eliminar_frame, text="codigo")
        self.eliminar_descripcion.grid(column=0, row=1, padx=5, pady=5)
        
        # Entry
        self.eliminar_var_entry1 = tk.StringVar()
        self.eliminar_entry1 = ttk.Entry(self.eliminar_frame,width=20, textvariable=self.eliminar_var_entry1)
        self.eliminar_entry1.grid(column=1,row=1, padx=5, pady=10)

        #button
        self.eliminar_button = ttk.Button(self.eliminar_frame, text="Eliminar", command=self.eliminar_sql)
        self.eliminar_button.grid(column=1, row=3, padx=10, pady=10)


    def eliminar_sql(self):
        dato = self.eliminar_var_entry1.get()
        elimina = self.bd.eliminar(dato)
        ms.showinfo("Eliminar", "Los campos fueron eliminados con éxito")

    def modificar(self):
        self.modificar_pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.modificar_pagina4, text="modificar")
        
        #labelFrame
        self.modificar_frame = ttk.Labelframe(self.modificar_pagina4, text="Modificar")
        self.modificar_frame.pack(padx=5, pady=5)

        # labels
        self.modifico_codigo = ttk.Label(self.modificar_frame, text="Ingrese el codigo del producto a modificar")
        self.modifico_codigo.grid(column=0, row=0,padx=5, pady=5, columnspan=2)
        
        self.modificar_codigo1 = ttk.Label(self.modificar_frame, text="Codigo")
        self.modificar_codigo1.grid(column=0, row=1,padx=5, pady=5)
        self.modificar_descripcion = ttk.Label(self.modificar_frame, text="Descripcion")
        self.modificar_descripcion.grid(column=0, row=2,padx=5, pady=5)
        self.modificar_precio = ttk.Label(self.modificar_frame, text="Precio")
        self.modificar_precio.grid(column=0, row=3,padx=5, pady=5)
        
        # Entry
        self.modificar_var_entry1 = tk.StringVar()
        self.modificar_entry1 = ttk.Entry(self.modificar_frame,width=20, textvariable=self.modificar_var_entry1)
        self.modificar_entry1.grid(column=1,row=1, padx=10, pady=5)
        
        self.modificar_var_entry2 = tk.StringVar()
        self.modificar_entry2 = ttk.Entry(self.modificar_frame,width=20, textvariable=self.modificar_var_entry2, state="readonly")
        self.modificar_entry2.grid(column=1,row=2, padx=10, pady=5)
        
        self.modificar_var_entry3 = tk.StringVar()
        self.modificar_entry3 = ttk.Entry(self.modificar_frame,width=20, textvariable=self.modificar_var_entry3, state="readonly")
        self.modificar_entry3.grid(column=1,row=3, padx=10, pady=5)

        #button
        self.modificar_button = ttk.Button(self.modificar_frame, text="Modificar", command=self.modificar_sql)
        self.modificar_button.grid(column=1, row=4, padx=10, pady=5)
        self.modificar_button2 = ttk.Button(self.modificar_frame, text="Comprobar", command=self.comprobar_sql)
        self.modificar_button2.grid(column=0, row=4, padx=10, pady=5)
    
    
    def modificar_sql(self):
        dato = self.modificar_var_entry1.get()
        descripcion = self.modificar_var_entry2.get()
        precio = self.modificar_var_entry3.get()
        modifica = self.bd.modificar(descripcion, precio, dato)

        ms.showinfo("Modificado", "Los datos fueron modificados correctamente")

        self.modificar_var_entry1.set("")
        self.modificar_var_entry2.set("")
        self.modificar_var_entry3.set("")
        self.modificar_entry2.config(state=DISABLED)
        self.modificar_entry3.config(state=DISABLED)


    def comprobar_sql(self):
        dato = self.modificar_var_entry1.get()
        self.entrada_bd = self.bd.consulta(dato)
        if self.entrada_bd==[]:
            ms.showerror("Error", "Ha ingresado un codigo inexistente! \n O no ha ingresado ninguno")
        else:
            self.modificar_entry2.config(state=NORMAL)
            self.modificar_entry3.config(state=NORMAL)
            self.modificar_var_entry2.set(self.entrada_bd[0][0])
            self.modificar_var_entry3.set(self.entrada_bd[0][1])

    def listado_completo(self):
        self.listado_pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.listado_pagina5, text="Listado completo de productos")

        #labelFrame
        self.listado_frame = ttk.LabelFrame(self.listado_pagina5, text="Listado completo")
        self.listado_frame.pack(padx=5, pady=5)

        #button
        self.listado_button = ttk.Button(self.listado_frame, text="listar", command=self.listar)
        self.listado_button.grid(column=0, row=0, padx=10, pady=10)
        
        #scrolledText
        self.listado_scrolledtext = st.ScrolledText(self.listado_frame, width=30, height=10, state=DISABLED)
        self.listado_scrolledtext.grid(column=0, row=1, padx=10, pady=10)

    def listar(self):
        lista = self.bd.listar()
        self.listado_scrolledtext.delete("1.0", tk.END)
        self.listado_scrolledtext.config(state=NORMAL)
        for articulos in lista:
            self.listado_scrolledtext.insert(tk.END, f"Codigo-{str(articulos[0])} \nDescripcion-{str(articulos[1])} \nprecio-{str(articulos[2])} \n")
        self.listado_scrolledtext.config(state=DISABLED)

app = App()
    
