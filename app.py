import tkinter as tk
import tkinter.ttk
from tkinter import ttk, messagebox, scrolledtext, filedialog
from tkinter import *
import sqlite3
import ia_lectora
from login import Logueo,Registro, email
from PIL import ImageTk, Image
from datetime import datetime,date, timedelta
import socket
import os
import sys
from ia_lectora import *
from escanear import *





class WilliamTheReader(tk.Tk):
    def db_consulta(self, consulta, parametros=()):
        with sqlite3.connect(self.db) as con:
            cursor = con.cursor()
            resultado = cursor.execute(consulta, parametros)
            con.commit()
        return resultado





    def __init__(self):
        super().__init__()

        #base de datos
        self.db = "database/cuentas.db"

        #Variables
        #Leemos el archivo en busca del email

        archivo = open("database\\localdata.txt", "r")
        self.email = archivo.read()
        archivo.close()
        print(self.email)

        #Otras variables
        self.password = None
        self.guardar_bool = False
        self.texto_escaneado = ""


        fecha_actual = datetime.today()
        print(fecha_actual)


        #Sacamos el estado logueado
        query = 'SELECT logueado FROM datos WHERE email = ?'
        registros_db = self.db_consulta(query,(self.email,))
        resultados = registros_db.fetchall()

        if resultados == []:
            self.logueado = False
        else:
            self.logueado = resultados[0][0]

        #Sacamos la id
        query = 'SELECT id FROM datos WHERE email = ?'
        registros_db = self.db_consulta(query,(self.email,))
        resultados = registros_db.fetchall()
        if resultados == []:
            pass
        else:
            self.id = resultados[0][0]

        #Sacamos el nombre
        query = 'SELECT nombre FROM datos WHERE email = ?'
        registros_db = self.db_consulta(query,(self.email,))
        resultados = registros_db.fetchall()
        if resultados == []:
            pass
        else:
            self.nombre = resultados[0][0]



        if self.logueado == False:
            self.loguearse()

        else:


            #estructura app principal
            height = 800
            width = 1600
            x = (self.winfo_screenwidth() // 2) - (width // 2)
            y = (self.winfo_screenheight() // 4) - (height // 4)
            self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
            self.wm_iconbitmap('assets\\william.ico')
            self.configure(bg="#FFFFFF")
            self.title("William The Reader")

            #Ventanas
            self.registro = None
            self.logueo = None

            # Barra superior
            barra_superior_label = Label(
                self,
                bg="#202123"
                #3D404B
            )
            barra_superior_label.place(width=200,height=800)



            #Cambio idiomas
            idiomas = [("Español", "assets\\spain.png"),("English", "assets\\US.png")]

            # Cargamos las imagenes como tuplas, (valor, imagen)
            self.opciones = []
            for idioma, imagen_path in idiomas:
                imagen = Image.open(imagen_path)
                imagen = imagen.resize((20, 20))
                imagen = ImageTk.PhotoImage(imagen)
                self.opciones.append((idioma, imagen))


            self.combobox_idiomas = ttk.Combobox(barra_superior_label, values=[opcion[0] for opcion in self.opciones])
            self.combobox_idiomas.place(x=30, y=600, width=100, height=35)
            self.combobox_idiomas.bind("<<ComboboxSelected>>", self.idioma)

            self.bandera = Label(bg="#202123", image=None)



            #Iidioma guardado en la db

            query = 'SELECT lg FROM datos WHERE email = ?'
            registros_db = self.db_consulta(query,(self.email,))
            resultados = registros_db.fetchall()
            if resultados == []:
                self.combobox_idiomas.set("English")
                print(self.combobox_idiomas.get())
                self.bandera.config(image=self.opciones[1][1])
                self.bandera.image = self.opciones[1][1]

                self.bandera.place(x=5, y=607)
            else:
                for dato in resultados:

                    if dato is not None:
                        self.idioma = dato[0]

                        self.combobox_idiomas.set(self.idioma)



                        if(self.idioma) == "Español":


                            self.bandera.config(image=self.opciones[0][1])
                            self.bandera.image = self.opciones[0][1]

                            self.bandera.place(x=5, y=607)

                        else:
                            self.bandera.config(image=self.opciones[1][1])
                            self.bandera.image = self.opciones[1][1]

                            self.bandera.place(x=5, y=607)






            #Detectar si esta logueado o no
            dias_maximos = timedelta(days=4)
            fecha_limite = fecha_actual - dias_maximos
            print(fecha_limite)
            query = 'SELECT lastlogin FROM datos WHERE email = ?'
            registros_db = self.db_consulta(query,(self.email,))
            resultados = registros_db.fetchall()

            for dato in resultados:

                if dato is not None:
                        lastlogin = datetime.strptime(dato[0], "%Y-%m-%d")


                        if lastlogin < fecha_limite or self.logueado == False:
                            self.logueado = False
                        elif lastlogin > fecha_limite and self.logueado != False:
                            self.logueado = True



                else:
                    self.logueado = False






            #Parte de la Ia narradora

            self.lectura_label = Label(
                self,
                bg="#FFFFFF"
            )
            self.lectura_label.place(x=500, y=0, width=900, height=800)

            self.lectura_entry_img = ImageTk.PhotoImage(file="assets\\entry.png")
            lectura_entry_label = Label(
                self.lectura_label,
                image=self.lectura_entry_img,
                bg="#FFFFFF"
            )
            lectura_entry_label.place(x=0, y=500, width=850, height=70)
            self.lectura_entry = Text(
                lectura_entry_label,
                bd=0,
                bg="#3D404B",
                highlightthickness=0,
                font=("yu gothic ui SemiBold", 16 * -1),fg="#FFFFFF", wrap="word"

            )
            self.lectura_entry.place(x=50, y=5, width=700, height=50)


            self.logo = ImageTk.PhotoImage(file="assets\\william.png")
            logo_label1 = Label(
                self.lectura_label,
                image=self.logo,
                bg="#FFFFFF"
            )
            logo_label1.place(x=380, y=100)

            logoText1 = Label(
                self.lectura_label,
                text="William The Reader",
                fg="#202123",
                font=("consolas bold", 20),
                bg="#FFFFFF"

            )
            logoText1.place(x=280, y=200)

            self.limitaciones = ImageTk.PhotoImage(file="assets\\exclamation.png")
            limitaciones_label1 = Label(
                self.lectura_label,
                image=self.limitaciones,
                bg="#FFFFFF"
            )
            limitaciones_label1.place(x=390, y=250)
            limitacionesText1 = Label(
                self.lectura_label,
                text="Limitations",
                fg="#202123",
                font=("consolas bold", 20),
                bg="#FFFFFF"

            )
            limitacionesText1.place(x=340, y=300)

            limitacionesText2 = Label(
                self.lectura_label,
                text="2000 character limit in one account.",
                fg="#202123",
                font=("consolas", 10),
                bg="#FFFFFF"

            )
            limitacionesText2.place(x=300, y=350)

            limitacionesText3 = Label(
                self.lectura_label,
                text="750 character limit in one text.",
                fg="#202123",
                font=("consolas", 10),
                bg="#FFFFFF"

            )
            limitacionesText3.place(x=300, y=370)

            limitacionesText4 = Label(
                self.lectura_label,
                text="Only images can be scanned.",
                fg="#202123",
                font=("consolas", 10),
                bg="#FFFFFF"

            )
            limitacionesText4.place(x=300, y=390)


            if self.idioma == "Español":
                limitacionesText1.config(text="Limitaciones")
                limitacionesText2.config(text="2000 caráctres son los permitidos en esta cuenta.")
                limitacionesText3.config(text="750 carácteres son los permitidos en un texto.")
                limitacionesText4.config(text="Solo imagenes pueden ser escaneadas.")



            #Boton escuchar texto
            if self.idioma == "Español":
                self.leer_imagen = PhotoImage(file="assets\\button_leer.png")
            else:
                self.leer_imagen = PhotoImage(file="assets\\button_read.png")

            self.boton_leer = tk.Button(
                self.lectura_label,
                image=self.leer_imagen,
                fg="#FFFFFF",
                font=("yu gothic ui Bold", 15 * -1),
                bg="#FFFFFF",
                bd=0,
                activebackground="#3D404B",
                cursor="hand2",
                command=self.leer
            )
            self.boton_leer.place(x=20, y=350, width=250, height=75)
            #Boton guardar texto, voz o ambas



            if self.idioma == "Español":
                self.guardar_imagen = PhotoImage(file="assets\\button_guardar.png")
            else:
                self.guardar_imagen = PhotoImage(file="assets\\button_save.png")

            self.boton_guardar = Button(
                self.lectura_label,
                image=self.guardar_imagen,
                fg="#206DB4",
                font=("yu gothic ui Bold", 15 * -1),
                bg="#FFFFFF",
                bd=0,
                activebackground="#3D404B",
                cursor="hand2",
                command=self.guardar_opciones
            )
            self.boton_guardar.place(x=300, y=650, width=250, height=75)

            #Boton escanear
            if self.idioma == "Español":
                self.escanear_imagen = PhotoImage(file="assets\\button_escanear.png")
            else:
                self.escanear_imagen = PhotoImage(file="assets\\button_scan.png")
            self.boton_escanear = Button(
                self.lectura_label,
                image=self.escanear_imagen,
                fg="#206DB4",
                font=("yu gothic ui Bold", 15 * -1),
                bg="#FFFFFF",
                bd=0,
                activebackground="#3D404B",
                cursor="hand2",
                command=self.subir_imagenes
            )
            self.boton_escanear.place(x=580, y=350, width=250, height=75)

            #Metodo de Strike
            if lastlogin != fecha_actual:
                ayer = (fecha_actual - timedelta(days=1)).date()

                if lastlogin.date() == ayer:

                    query = 'SELECT strike FROM datos WHERE email = ?'
                    registros_db = self.db_consulta(query, (self.email,))
                    strike = registros_db.fetchall()


                    query = 'UPDATE datos SET strike = ? WHERE email = ?'
                    registros_db = self.db_consulta(query, (strike[0][0]+1, self.email))
                    if strike != 1:
                        if self.idioma == "Español":
                            self.mensaje("¡Enhorabuena!","Llevas una racha de {} días.".format(strike[0][0]+1))
                        else:
                            self.mensaje("¡Congratulations!","You are now in a strike of {} days".format(strike[0][0]+1))
                    else:
                        if self.idioma == "Español":
                            self.mensaje("¡Enhorabuena!","Llevas una racha de {} día.".format(strike[0][0]+1))
                        else:
                            self.mensaje("¡Congratulations!","You are now in a strike of {} day".format(strike[0][0]+1))


                elif lastlogin.date() < ayer:

                    query = 'UPDATE datos SET strike = ? WHERE email = ?'
                    registros_db = self.db_consulta(query, (0, self.email))


                query = 'UPDATE datos SET lastlogin = ? WHERE email = ?'
                registros_db = self.db_consulta(query, (date.today(), self.email))





                #Perfil
                #Foto de perfil
                if self.id % 2 == 0:


                    self.perfil_imagen = ImageTk.PhotoImage(file="assets\\animal1.png")

                if self.id % 2 != 0:


                    self.perfil_imagen = ImageTk.PhotoImage(file="assets\\animal2.png")

                #Perfil en general

                self.perfil_menu = Menubutton(
                    barra_superior_label,
                    image=self.perfil_imagen,
                    borderwidth=0,
                    highlightthickness=0,
                    relief="flat",
                    activebackground="#272A37",
                    cursor="hand2",
                    bg="#202123"
                )
                self.perfil_menu.place(x=10, y=700, width=89, height=83)
                self.perfil_menu.menub = Menu(self.perfil_menu, tearoff=0)
                self.perfil_menu["menu"] = self.perfil_menu.menub

                perfilText1 = Label(
                    barra_superior_label,
                    text=self.nombre,
                    fg="#FFFFFF",
                    font=("consolas bold", 15),
                    bg="#202123"

                )
                perfilText1.place(x=92, y=725)


                if self.idioma == "Español":
                    self.perfil_menu.menub.add_checkbutton(label='Editar', command=self.editar)
                    self.perfil_menu.menub.add_checkbutton(label='Cerrar sesión', command=self.cerrar_sesion)
                else:
                    self.perfil_menu.menub.add_checkbutton(label='Edit', command=self.editar)
                    self.perfil_menu.menub.add_checkbutton(label='Log out', command=self.cerrar_sesion)





    #Metodo Strike

    def mensaje(self,texto,texto2):
        self.mensajes_img = PhotoImage(file="assets\\emaiL.png")
        self.mensajes_label = Label(
            self,
            image=self.mensajes_img,
            bg="#FFFFFF"

        )
        self.mensajes_label.place(x=220 ,y= 50, width=411, height=54)

        self.william = PhotoImage(file="assets\\william_message.png")
        mensaje_img = Label(
            self.mensajes_label,
            image=self.william,
            bg="#3D404B"
        )
        mensaje_img.place(x=5, y=3)
        self.mensajetexto1 = Label(
            self.mensajes_label,
            text=texto,
            fg="#FFFFFF",
            font=("consolas bold", 15),
            bg="#3D404B"

        )
        self.mensajetexto1.place(x=36, y=5)

        self.mensajetexto2 = Label(
            self.mensajes_label,
            text=texto2,
            fg="#FFFFFF",
            font=("consolas bold", 10),
            bg="#3D404B"

        )
        self.mensajetexto2.place(x=36, y=30)


    #Perfil


    def cerrar_sesion(self):

        self.logueado = False
        query = 'UPDATE datos SET logueado = ? WHERE email = ?'


        registros_db = self.db_consulta(query, (self.logueado, self.email))
        self.destroy()
        os.system("python app.py")



        # Ajustes

    def cambiar_datos(self):

        if self.new_lastname_entry.get() != "":
            query = 'UPDATE datos SET apellidos = ? WHERE email = ?'

            registros_db = self.db_consulta(query, (self.new_lastname_entry.get(), self.email))
            self.destroy()
            os.system("python app.py")

        if self.new_name_entry.get() != "":
            query = 'UPDATE datos SET nombre = ? WHERE email = ?'

            registros_db = self.db_consulta(query, (self.new_name_entry.get(), self.email))
            self.destroy()
            os.system("python app.py")

        if self.new_email_entry.get() != "":
            query = 'UPDATE datos SET email = ? WHERE email = ?'

            registros_db = self.db_consulta(query, (self.new_email_entry.get(), self.email))
            archivo = open("database\\localdata.txt", "w")
            archivo.write(self.new_email_entry.get())
            archivo.close()

            self.destroy()
            os.system("python app.py")

    def editar(self):




        v = Toplevel()
        v.wm_iconbitmap('assets\\william.ico')
        window_width = 350
        window_height = 450
        screen_width = v.winfo_screenwidth()
        screen_height = v.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        v.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        # win.iconbitmap('images\\aa.ico')
        v.configure(background='#272A37')
        v.resizable(False, False)

        # ====== Email ====================
        self.new_email_entry = Entry(v, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                             bd=0)
        self.new_email_entry.place(x=40, y=40, width=256, height=50)
        self.new_email_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        new_email_label = Label(v, text='• Email', fg="#FFFFFF", bg='#272A37',
                             font=("yu gothic ui", 11, 'bold'))
        new_email_label.place(x=40, y=10)

        # Nombre
        self.new_name_entry = Entry(v, bg="#3D404B", font=("yu gothic ui semibold", 12),
                                   highlightthickness=1,
                                   bd=0
                                   )
        self.new_name_entry.place(x=40, y=140, width=256, height=50)
        self.new_name_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        new_name_label = Label(v, text='• Name', fg="#FFFFFF", bg='#272A37',
                                   font=("yu gothic ui", 11, 'bold'))
        new_name_label.place(x=40, y=110)

        # Apellidos
        self.new_lastname_entry = Entry(v, bg="#3D404B", font=("yu gothic ui semibold", 12),
                                   highlightthickness=1,
                                   bd=0
                                   )
        self.new_lastname_entry.place(x=40, y=240, width=256, height=50)
        self.new_lastname_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        new_lastname_label = Label(v, text='• Last Name', fg="#FFFFFF", bg='#272A37',
                                   font=("yu gothic ui", 11, 'bold'))
        new_lastname_label.place(x=40, y=210)

        # Update
        update_dt = Button(v, fg='#f8f8f8', text='Update', bg='#1D90F5',
                             font=("yu gothic ui", 12, "bold"),
                             cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5",command=self.cambiar_datos)
        update_dt.place(x=40, y=320, width=256, height=45)

        if self.idioma == "Español":
            v.title('Editar')
            new_name_label.config(text='• Nombre')
            new_lastname_label.config(text='• Apellidos')
            new_email_label.config(text='• Email')
            update_dt.config(text='Actualizar')

        else:
            v.title('Edit')












    #Idioma
    def idioma(self, event):

        self.seleccion = self.combobox_idiomas.get()
        if self.seleccion == "Español":
            self.bandera.config(image=self.opciones[0][1])
            self.bandera.image = self.opciones[0][1]  # Guardar una referencia a la imagen para evitar que sea eliminada por la recolección de basura

            self.bandera.place(x=970, y=30)  # Ajustar la posición de las imágenes
            self.cambiar_idioma_db("Español")
            self.destroy()
            os.system("python app.py")


        else:
            self.bandera.config(image=self.opciones[1][1])
            self.bandera.image = self.opciones[1][1]  # Guardar una referencia a la imagen para evitar que sea eliminada por la recolección de basura

            self.bandera.place(x=970, y=30)  # Ajustar la posición de las imágenes
            self.cambiar_idioma_db("English")
            self.destroy()
            os.system("python app.py")

    def cambiar_idioma_db(self, idioma):
        query = 'SELECT email FROM datos WHERE email = ?'
        registros_db = self.db_consulta(query,(self.email,))
        resultados = registros_db.fetchall()
        for dato in resultados:
                query = 'UPDATE datos SET lg = ? WHERE email = ?'


                registros_db = self.db_consulta(query,(idioma,self.email))


    #Loguearse

    def loguearse(self):

        self.withdraw()
        self.logueo = Logueo()
        self.wait_window()
        self.cerrar_sesion_var = False




    # IA Lectora

    def leer(self):

        query = 'SELECT limite FROM datos WHERE email = ?'
        registros_db = self.db_consulta(query, (self.email,))
        resultados = registros_db.fetchall()
        self.limite = resultados[0][0]

        if len(self.lectura_entry.get("1.0", "end-1c")) > 0:
            if ( self.limite - len(self.lectura_entry.get("1.0", "end-1c"))) >= 0:
                if len(self.lectura_entry.get("1.0", "end-1c")) > 750:
                    if self.idioma == 'Español':
                        messagebox.showerror(message="Has sobrepasado el limite de palabras en un texto.", title="Error")
                    else:
                        messagebox.showerror(message="You have exceeded the word limit in a text.", title="Error")
                else:
                    ia_lectora.leer(self.lectura_entry.get("1.0", "end-1c"))



                    query = 'UPDATE datos SET limite = ? WHERE email = ?'
                    limite_actual = self.limite - len(self.lectura_entry.get("1.0", "end-1c"))
                    registros_db = self.db_consulta(query, (limite_actual, self.email))

        else:
            if self.idioma == 'Español':
                messagebox.showerror(message="Porfavor introduzca palabras.", title="Error")
            else:
                messagebox.showerror(message="Please put words.", title="Error")


    #Escaneo imagenes
    def escanear(self,imagen):
        self.texto_escaneado = escanear_ocr(imagen)
        self.lectura_entry.delete(1.0, tk.END)
        self.lectura_entry.insert(tk.END, self.texto_escaneado)

    def subir_imagenes(self):
        self.ruta_imagen = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;")])
        if self.ruta_imagen != "":
            self.escanear(imagen= self.ruta_imagen)

    #Guardar archivos
    def guardar_opciones(self):
        win = Toplevel()
        win.wm_iconbitmap('assets\\william.ico')
        window_width = 350
        window_height = 350
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')


        win.transient(self)

        win.configure(background='#272A37')

        # Boton guardar texto

        texto = Button(win, fg='#f8f8f8', bg='#1D90F5',
                             text="",
                             font=("yu gothic ui", 12, "bold"),
                             cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5", command=self.guardar_texto
                      )

        texto.place(x=40, y=140, width=256, height=45)
        # Boton guardar audio

        audio = Button(win, fg='#f8f8f8', bg='#1D90F5',
                             text="",
                             font=("yu gothic ui", 12, "bold"),
                             cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5", command= self.guardar_audio)
        audio.place(x=40, y=200, width=256, height=45)
        # Boton guardar texto

        todo = Button(win, fg='#f8f8f8', bg='#1D90F5',
                             text="",
                             font=("yu gothic ui", 12, "bold"),
                             cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5", command= self.guardar_todo)
        todo.place(x=40, y=260, width=256, height=45)


        if self.idioma == "Español":
            win.title('Guardar')

            texto.config(text="Guardar Texto")
            todo.config(text="Guardar Texto y Audio")
            audio.config(text="Guardar Audio")
        else:
            win.title('Save')

            texto.config(text="Save Text")
            todo.config(text="Save Text and Audio")
            audio.config(text="Save Audio")




    def guardar_texto(self):
        self.guardado_texto = True


        if len(self.lectura_entry.get("1.0", "end-1c")) > 0:
            archivo_guardado = filedialog.asksaveasfilename(defaultextension=".txt",
                                                            filetypes=[("Archivos de texto", "*.txt")])
            if archivo_guardado:
                try:
                    archivo = open(archivo_guardado, "x", encoding="utf-8")
                    contenido = self.lectura_entry.get("1.0", tk.END)
                    archivo.write(contenido)
                    archivo.close()

                    # Esto distingue entre si se guardara ambos archivos o solo uno
                    if self.guardar_bool != True:

                        if self.idioma == 'Español':
                            messagebox.showinfo(
                                message="Solo se ha guardado un archivo en el escritorio ya que no se ha seleccionado el audio.",
                                title="William The Reader")

                        else:
                            messagebox.showinfo(
                                message="Only one file in the Desktop has been saved as no audio has been selected.",
                                title="William The Reader")

                except FileExistsError:
                    #Comunicamos a traves de un booleano que no se ha podido guardar el archivo
                    self.guardado_texto = False
                    if self.idioma == 'Español':
                        messagebox.showerror(message="Ya existe un archivo a ese nombre, borrelo si desea.", title="Error")
                    else:
                        messagebox.showerror(message="There is a file with that name, delete it if you want.", title="Error")






        else:
            if self.idioma == 'Español':
                messagebox.showerror(message="Porfavor introduzca palabras.", title="Error")

            else:
                messagebox.showerror(message="Please put words.", title="Error")





    def guardar_audio(self):

        if len(self.lectura_entry.get("1.0", "end-1c")) > 0:
            archivo_guardado = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                            filetypes=[("Archivos de texto", "*.mp3")])

            if archivo_guardado:
                # Llamar a la funcion guardar_audio_ia del archivo ia_lectora

                guardar_audio_ia(self.lectura_entry.get("1.0", "end-1c"), archivo_guardado)

            if self.guardar_bool != True:

                if self.idioma == 'Español':
                    messagebox.showinfo(message="Solo se ha guardado un archivo mp3 ya que no se ha seleccionado el texto.",
                                        title="William The Reader")

                else:
                    messagebox.showinfo(message="Only one file mp3 has been saved as no text has been selected.",
                                        title="William The Reader")



        else:
            if self.idioma == 'Español':
                messagebox.showerror(message="Porfavor introduzca palabras.", title="Error")

            else:
                messagebox.showerror(message="Please put words.", title="Error")



    def guardar_todo(self):
        self.guardar_bool = True

        if len(self.lectura_entry.get("1.0", "end-1c")) > 0:
            # Llamar a la funcion guardar_audio_ia del archivo ia_lectora
            self.guardar_audio()
            self.guardar_texto()

            if self.guardado_texto == True:


                if self.idioma == 'Español':
                    messagebox.showinfo(message="Se han guardado todos los archivos, texto y mp3.",
                                        title="William The Reader")

                else:
                    messagebox.showinfo(message="All files have been saved, text and mp3.",
                                        title="William The Reader")

            else:

                if self.idioma == 'Español':
                    messagebox.showinfo(message="Solo se ha guardado un archivo mp3 ya que ha sucedido un error con el archivo texto.",
                                        title="William The Reader")

                else:
                    messagebox.showinfo(message="Only one file mp3 has been saved as an error appear with the text file.",
                                        title="William The Reader")

        else:
            if self.idioma == 'Español':
                messagebox.showerror(message="Porfavor introduzca palabras.", title="Error")

            else:
                messagebox.showerror(message="Please put words.", title="Error")




if __name__ == '__main__':
    app = WilliamTheReader()
    app.mainloop()
