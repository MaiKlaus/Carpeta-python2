import tkinter as tk
import sys

class Aplicacion:
    def __init__(self):
        self.nombres=[]
        self.telefonos=[]
        self.mails=[]
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="¡Bienvenido a su agenda!")
        self.label1.grid(column=1, row=0)
        self.boton1=tk.Button(self.ventana1,text="Agregar un contacto",command=self.agregar_contacto)
        self.boton1.grid(column=1,row=1)
        self.boton2=tk.Button(self.ventana1,text="Lista de contactos",command=self.lista_contactos)
        self.boton2.grid(column=1,row=2)
        self.boton3=tk.Button(self.ventana1,text="Consultar contacto",command=self.consultar_contacto)
        self.boton3.grid(column=1,row=3)
        self.boton4=tk.Button(self.ventana1,text="Modificar contacto",command=self.modificar_contacto)
        self.boton4.grid(column=1,row=4)
        self.boton5=tk.Button(self.ventana1,text="Finalizar programa",command=self.fin_programa)
        self.boton5.grid(column=1,row=5)
        self.ventana1.mainloop()

    def agregar_contacto(self):
        self.ventana2=tk.Tk()
        self.ventana2.title("Agregar un contacto")
        self.label1=tk.Label(self.ventana2,text="Contacto nuevo:")
        self.label1.grid(column=0, row=0)
        self.label2=tk.Label(self.ventana2,text="Nombre:")
        self.label2.grid(column=0, row=1)
        self.nombre=tk.StringVar(self.ventana2)
        self.entry1=tk.Entry(self.ventana2, width=20, textvariable=self.nombre)      
        self.entry1.grid(column=1, row=1)
        self.label3=tk.Label(self.ventana2,text="Teléfono:")
        self.label3.grid(column=0, row=2)
        self.telefono=tk.StringVar(self.ventana2)
        self.entry2=tk.Entry(self.ventana2, width=20, textvariable=self.telefono)      
        self.entry2.grid(column=1, row=2)
        self.label4=tk.Label(self.ventana2,text="Mail:")
        self.label4.grid(column=0, row=3)
        self.correo=tk.StringVar(self.ventana2)
        self.entry3=tk.Entry(self.ventana2, width=20, textvariable=self.correo)      
        self.entry3.grid(column=1, row=3)
        self.boton6=tk.Button(self.ventana2, text="Cargar", command=self.carga)
        self.boton6.grid(column=1,row=4)
        self.ventana2.mainloop()
    def carga(self):
        nomb = self.nombre.get()
        self.nombres.append(nomb)
        telefon = self.telefono.get()
        self.telefonos.append(int(telefon))
        corre = self.correo.get()
        self.mails.append(str(corre))
        self.nombre.set("")
        self.telefono.set("")
        self.correo.set("")

    def lista_contactos(self):
        self.ventana3=tk.Tk()
        self.ventana3.title("Lista de contactos")
        for x in range(len(self.nombres)):
            self.label1=tk.Label(self.ventana3,text="Lista de contactos")
            self.label1.grid(column=1, row=0)
            self.label2=tk.Label(self.ventana3,text="Nombre")
            self.label2.grid(column=0, row=1)
            self.label_nombre = tk.Label(self.ventana3, text=self.nombres[x])
            self.label_nombre.grid(column=0, row=x+2)
            self.label3=tk.Label(self.ventana3,text="Teléfono")
            self.label3.grid(column=1, row=1)            
            self.label_telefono = tk.Label(self.ventana3, text=self.telefonos[x])
            self.label_telefono.grid(column=1, row=x+2)
            self.label3=tk.Label(self.ventana3,text="Correo electrónico")
            self.label3.grid(column=2, row=1)                 
            self.label_correo = tk.Label(self.ventana3, text=self.mails[x])
            self.label_correo.grid(column=2, row=x+2)
        self.ventana3.mainloop()

    def consultar_contacto(self):
        self.ventana4=tk.Tk()
        self.ventana4.title("Consulta de contacto")
        self.label1=tk.Label(self.ventana4,text="¿Qué contacto desea consultar?")
        self.label1.grid(column=1,row=0)
        self.consulta=tk.StringVar(self.ventana4)
        self.entry1=tk.Entry(self.ventana4, width=20, textvariable=self.consulta)
        self.entry1.grid(column=1,row=1)
        self.boton7=tk.Button(self.ventana4, text="Consultar", command=self.consultar)
        self.boton7.grid(column=1,row=2)
        self.ventana4.mainloop()

    def consultar(self):
        n = self.consulta.get()
        self.ventana5=tk.Tk()
        self.ventana5.title("Consulta de contacto")
        for x in range(len(self.nombres)):
            if n == self.nombres[x]:
                self.label1=tk.Label(self.ventana5,text="Nombre:")
                self.label1.grid(column=0, row=0)
                self.label2=tk.Label(self.ventana5,text=self.nombres[x])
                self.label2.grid(column=1,row=0)
                self.label3=tk.Label(self.ventana5,text="Teléfono:")
                self.label3.grid(column=0,row=1)
                self.label4=tk.Label(self.ventana5,text=self.telefonos[x])
                self.label4.grid(column=1,row=1)
                self.label5=tk.Label(self.ventana5,text="Mail:")
                self.label5.grid(column=0,row=2)
                self.label6=tk.Label(self.ventana5,text=self.mails[x])
                self.label6.grid(column=1,row=2)
        self.ventana5.mainloop()

    def modificar_contacto(self):
        self.ventana6=tk.Tk()
        self.ventana6.title("Modificar contacto")
        self.label1=tk.Label(self.ventana6,text="¿Qué contacto desea modificar?")
        self.label1.grid(column=1,row=0)
        self.modificacion=tk.StringVar(self.ventana6)
        self.entry1=tk.Entry(self.ventana6, width=20, textvariable=self.modificacion)
        self.entry1.grid(column=1,row=1)
        self.boton7=tk.Button(self.ventana6, text="Modificar", command=self.modificar)
        self.boton7.grid(column=1,row=2)
        self.ventana6.mainloop()
    def modificar(self):
        m = self.modificacion.get()
        self.ventana7=tk.Tk()
        self.ventana7.title("Modificación de contacto")
        for x in range(len(self.nombres)):
            if self.nombres[x] == m:
                self.label1=tk.Label(self.ventana7,text=m)
                self.label1.grid(column=1,row=0)
                self.label2=tk.Label(self.ventana7,text="Ingrese el nuevo número de teléfono: ")
                self.label2.grid(column=0,row=1)
                self.telefono_nuevo=tk.StringVar(self.ventana7)
                self.entry1=tk.Entry(self.ventana7, width=20,textvariable=self.telefono_nuevo)
                self.entry1.grid(column=1,row=1)
                self.label3=tk.Label(self.ventana7,text="Ingrese el nuevo mail: ")
                self.label3.grid(column=0,row=2)
                self.correo_nuevo=tk.StringVar(self.ventana7)
                self.entry2=tk.Entry(self.ventana7, width=20,textvariable=self.correo_nuevo)
                self.entry2.grid(column=1,row=2)
                self.boton1=tk.Button(self.ventana7, text="Actualizar", command=self.actualizar_contacto)
                self.boton1.grid(column=1,row=3)
        self.ventana7.mainloop()
    def actualizar_contacto(self):
            nombre_modificar = self.modificacion.get()
            nuevo_telefono = self.telefono_nuevo.get()
            nuevo_correo = self.correo_nuevo.get()
            self.telefono_nuevo.set("")
            self.correo_nuevo.set("")
            for x in range(len(self.nombres)):
                if self.nombres[x] == nombre_modificar:
                    self.telefonos[x] = int(nuevo_telefono)
                    self.mails[x] = str(nuevo_correo)

    def fin_programa(self):
        sys.exit(0)

app=Aplicacion()