from tkinter import ttk, messagebox
import sqlite3
from tkinter import *
from PIL import ImageTk, Image
from datetime import date
import socket
import os
import sys
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

#Variables globales
idioma = None

db = "database/cuentas.db"


def db_consulta(consulta, parametros=()):
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        resultado = cursor.execute(consulta, parametros)
        con.commit()
    return resultado


archivo = open("database\\localdata.txt", "r")
email = archivo.read()
archivo.close()

query = 'SELECT lg FROM datos WHERE email = ?'
registros_db = db_consulta(query,(email,))
resultados = registros_db.fetchall()
for dato in resultados:

    if dato is not None:
            idioma = dato[0]


            if(idioma) == "Español":
                idioma = "Español"

            else:
                idioma = "English"


######################Logueo###################
class Logueo(Toplevel):
    def __init__(self):
        super().__init__()
        #base de datos
        query = 'SELECT logueado FROM datos WHERE email = ?'
        registros_db = db_consulta(query,(email,))
        resultados = registros_db.fetchall()
        if resultados == []:
            self.logueado = False
        else:
            self.logueado = resultados[0][0]
        #Ventanas
        self.registro = None


        #Ventana principal
        self.wm_iconbitmap('assets\\william.ico')
        self.title("William The Reader")
        height = 650
        width = 1240
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 4) - (height // 4)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.configure(bg="#FFFFFF")
        #Imagen derecha
        self.image_1 = PhotoImage(file="assets\\image_1.png")
        self.image_1_label = Label(
            self,
            image=self.image_1,
            bg="#FFFFFF"
        )
        self.image_1_label.place(x=300, y=-300)
        # Logo y texto
        self.Login_logo = ImageTk.PhotoImage(file="assets\\william.png")
        self.Login_logo_label1 = Label(
            self,
            image=self.Login_logo,
            bg="#FFFFFF"
        )
        self.Login_logo_label1.place(x=60, y=35)

        self.Login_logoText1 = Label(
            self,
            text="William The Reader",
            fg="#373737",
            font=("consolas bold", 30),
            bg="#FFFFFF"

        )
        self.Login_logoText1.place(x=150, y=45)


        # Login
        self.login_text1 = Label(
            self,
            text="Login to continue",
            fg="#373737",
            font=("yu gothic ui Bold", 28 * -1),
            bg="#FFFFFF"

        )
        self.login_text1.place(x=75, y=121)

        # No miembro
        self.login_text2 = Label(
            self,
            text="Not a member?",
            fg="#373737",
            font=("yu gothic ui Regular", 15 * -1),
            bg="#FFFFFF"
        )
        self.login_text2.place(x=75, y=187)

        # Ve a registrarse
        self.registrarse_boton = Button(
            self,
            text="Sign Up",
            fg="#206DB4",
            font=("yu gothic ui Bold", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            cursor="hand2",
            activebackground="#272A37",
            activeforeground="#ffffff",
            command= self.registrar
        )
        self.registrarse_boton.place(x=235, y=185, width=75, height=35)


        # Email
        self.Login_emailName_image = PhotoImage(file="assets\\email.png")
        self.Login_emailName_image_Label = Label(
            self,
            image=self.Login_emailName_image,
            bg="#FFFFFF"

        )
        self.Login_emailName_image_Label.place(x=76, y=242)

        self.Login_emailName_text = Label(
            self.Login_emailName_image_Label,
            text="Email account",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.Login_emailName_text.place(x=25, y=0)

        self.Login_emailName_icon = PhotoImage(file="assets\\email-icon.png")
        self.Login_emailName_icon_Label = Label(
            self.Login_emailName_image_Label,
            image=self.Login_emailName_icon,
            bg="#3D404B"
        )
        self.Login_emailName_icon_Label.place(x=370, y=15)

        self.Login_emailName_entry = Entry(
            self.Login_emailName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1)
        )
        self.Login_emailName_entry.place(x=8, y=17, width=354, height=27)


        # Contraseña
        self.Login_passwordName_image = PhotoImage(file="assets\\email.png")
        self.Login_passwordName_image_Label = Label(
            self,
            image=self.Login_passwordName_image,
            bg="#FFFFFF"
        )
        self.Login_passwordName_image_Label.place(x=80, y=330)

        self.Login_passwordName_text = Label(
            self.Login_passwordName_image_Label,
            text="Password",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.Login_passwordName_text.place(x=25, y=0)

        self.Login_passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
        self.Login_passwordName_icon_Label = Label(
            self.Login_passwordName_image_Label,
            image=self.Login_passwordName_icon,
            bg="#3D404B"
        )
        self.Login_passwordName_icon_Label.place(x=370, y=15)

        self.Login_passwordName_entry = Entry(
            self.Login_passwordName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
            show="*"
        )
        self.Login_passwordName_entry.place(x=8, y=17, width=354, height=27)

        # Submit
        self.Login_button_image_1 = PhotoImage(file="assets\\button_1.png")
        Login_button_1 = Button(
            self,
            image=self.Login_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            #command=lambda:,
            relief="flat",
            activebackground="#FFFFFF",
            activeforeground="#FFFFFF",
            cursor="hand2",
            command=self.verificacion_logueo
        )
        Login_button_1.place(x=120, y=445, width=333, height=65)

        # Olvidar contraseña
        self.forgotPassword = Button(
            self,
            text="Forgot Password",
            fg="#206DB4",
            font=("yu gothic ui Bold", 15 * -1),
            bg="#FFFFFF",
            bd=0,
            activebackground="#FFFFFF",
            activeforeground="#FFFFFF",
            cursor="hand2",
            command=self.forgot_password
        )
        self.forgotPassword.place(x=210, y=400, width=200, height=35)

        #Traduccion
        self.traducir()




    def traducir(self):
        query = 'SELECT lg FROM datos WHERE email = ?'
        registros_db = db_consulta(query, (email,))
        resultados = registros_db.fetchall()

        if resultados != []:
            for dato in resultados:
                self.idioma = dato[0]
                if self.idioma == "Español":
                    self.login_text1.config(text="Loguear para continuar")
                    self.login_text2.config(text="¿No eres un miembro?")
                    self.registrarse_boton.config(text="Registrarse")
                    self.Login_emailName_text.config(text="Email")
                    self.Login_passwordName_text.config(text="Contraseña")
                    self.forgotPassword.config(text="¿Olvidastes la contraseña?")

    def registrar(self):

        self.registro = Registro()
        self.destroy()
    def verificacion_logueo(self):
        self.email = self.Login_emailName_entry.get()
        self.password = self.Login_passwordName_entry.get()
        #Buscamos el email y seleccionamos la contraseña
        query = 'SELECT password FROM datos WHERE email = ?'
        registros_db = db_consulta(query, (self.email,))
        resultados = registros_db.fetchall()
        #Si no hay resultados
        if resultados==[]:
            if idioma == "English":
                messagebox.showerror(message="That account does not exist in our database", title="Error")
            else:
                messagebox.showerror(message="Esa cuenta no existe en nuestra base de datos.", title="Error")

        # Si sí hay
        else:
            for password in resultados:

                if check_password_hash(password[0], self.password):

                    # Escribimos el email en un archivo de localdata para asi poder utilizarlo en otros archivos sin problema alguno
                    # Si queremos buscarlo en la base de datos y hay varias ips asociadas a distintos emails habra un error y se confundira entre cuentas

                    archivo = open("database\\localdata.txt", "w")
                    archivo.write(self.email)
                    archivo.close()

                    #Cambiamos datos de la base de datos para que en la app principal aparezca logueado

                    query = 'UPDATE datos SET lastlogin = ? WHERE email = ?'
                    registros_db = db_consulta(query, (date.today(), self.email))
                    query = 'UPDATE datos SET logueado = ? WHERE email = ?'
                    registros_db = db_consulta(query, (True, self.email))

                    #Salimos y abrimos la app principal
                    self.destroy()
                    os.system("python app.py")

                #Error
                else:
                    if idioma == "English":
                        messagebox.showerror(message="Incorrect password",title="Error")
                    else:
                        messagebox.showerror(message="Contraseña incorrecta",title="Error")

    def forgot_password(self):
        self.fp = Toplevel()
        self.fp.wm_iconbitmap('assets\\william.ico')
        window_width = 350
        window_height = 500
        screen_width = self.fp.winfo_screenwidth()
        screen_height = self.fp.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        self.fp.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        self.fp.title('Forgot Password')
        # win.iconbitmap('images\\aa.ico')
        self.fp.configure(background='#272A37')
        self.fp.resizable(False, False)

        # ====== Email ====================
        self.email_entry3 = Entry(self.fp, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                             bd=0)
        self.email_entry3.place(x=40, y=80, width=256, height=50)
        self.email_entry3.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        self.email_label3 = Label(self.fp, text='• Email', fg="#FFFFFF", bg='#272A37',
                             font=("yu gothic ui", 11, 'bold'))
        self.email_label3.place(x=40, y=50)

        # ====== Question ====================
        self.question_entry = Entry(self.fp, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                             bd=0)
        self.question_entry.place(x=40, y=180, width=256, height=50)
        self.question_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        self.question_label = Label(self.fp, text='• Where were you born?', fg="#FFFFFF", bg='#272A37',
                             font=("yu gothic ui", 11, 'bold'))
        self.question_label.place(x=40, y=150)

        # ====  New Password ==================
        self.new_password_entry = Entry(self.fp, bg="#3D404B", font=("yu gothic ui semibold", 12), show='•',
                                   highlightthickness=1,
                                   bd=0
                                   )
        self.new_password_entry.place(x=40, y=280, width=256, height=50)
        self.new_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        self.new_password_label = Label(self.fp, text='• New Password', fg="#FFFFFF", bg='#272A37',
                                   font=("yu gothic ui", 11, 'bold'))
        self.new_password_label.place(x=40, y=250)

        # ======= Update password Button ============
        self.update_pass = Button(self.fp, fg='#f8f8f8', text='Update Password', bg='#1D90F5',
                             font=("yu gothic ui", 12, "bold"),
                             cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5",command=self.actualizar_password)
        self.update_pass.place(x=40, y=400, width=256, height=45)
        if self.idioma == "Español":

            self.question_label.config(text="¿Donde nacistes?")
            self.new_password_label.config(text="Nueva contraseña")
            self.update_pass.config(text="Actualizala")




    def actualizar_password(self):
        query = 'SELECT question FROM datos WHERE email = ?'
        registros_db = db_consulta(query, (self.email_entry3.get(),))
        resultados = registros_db.fetchall()
        self.question = resultados[0][0]

        if self.question == self.question_entry.get():
            query = 'UPDATE datos SET password = ? WHERE email = ?'
            password = generate_password_hash(self.new_password_entry.get(), 'pbkdf2:sha256:30', 45)
            registros_db = db_consulta(query, (password, self.email_entry3.get()))
            self.fp.destroy()
            self.destroy()
            os.system("python app.py")





#################Registro###########

class Registro(Toplevel):
    def __init__(self):  # Cambia el nombre de la variable para evitar conflictos con el nombre de la clase
        super().__init__()

        # Ventanas
        self.logueo = None


        #Ventana principal

        self.wm_iconbitmap('assets\\william.ico')
        self.title("William The Reader")
        height = 650
        width = 1240
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 4) - (height // 4)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.configure(bg="#FFFFFF")


        #Imagen derecha
        self.image_1 = PhotoImage(file="assets\\image_1.png")
        image_1_label = Label(
            self,
            image=self.image_1,
            bg="#FFFFFF"
        )
        image_1_label.place(x=300, y=-300)

        # Logo y texto
        self.Login_logo = PhotoImage(file="assets\\william.png")
        Login_logo_label1 = Label(
            self,
            image=self.Login_logo,
            bg="#FFFFFF"
        )
        Login_logo_label1.place(x=60, y=35)

        Login_logoText1 = Label(
            self,
            text="William The Reader",
            fg="#373737",
            font=("consolas bold", 30),
            bg="#FFFFFF"

        )
        Login_logoText1.place(x=150, y=45)


        # Register
        self.register = Label(
            self,
            text="Create new account",
            fg="#373737",
            font=("yu gothic ui Bold", 28 * -1),
            bg="#FFFFFF"
        )
        self.register.place(x=75, y=121)

        # Ya tiene cuenta
        self.text = Label(
            self,
            text="Already a member?",
            fg="#373737",
            font=("yu gothic ui Regular", 15 * -1),
            bg="#FFFFFF"
        )
        self.text.place(x=75, y=187)

        # Ve a loguearte
        self.loguearse = Button(
            self,
            text="Login",
            fg="#206DB4",
            font=("yu gothic ui Bold", 15 * -1),
            bd=0,
            bg="#FFFFFF",
            cursor="hand2",
            activebackground="#272A37",
            activeforeground="#ffffff",
            command=self.loguearse
        )
        self.loguearse.place(x=220, y=185, width=70, height=35)


        # Nombre
        self.firstName_image = PhotoImage(file="assets\\input_img.png")
        firstName_image_Label = Label(
            self,
            image=self.firstName_image,
            bg="#FFFFFF"
        )
        firstName_image_Label.place(x=80, y=242)

        self.firstName_text = Label(
            firstName_image_Label,
            text="First name",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.firstName_text.place(x=25, y=0)

        self.firstName_icon = PhotoImage(file="assets\\name_icon.png")
        firstName_icon_Label = Label(
            firstName_image_Label,
            image=self.firstName_icon,
            bg="#3D404B"
        )
        firstName_icon_Label.place(x=159, y=15)

        self.firstName_entry = Entry(
            firstName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.firstName_entry.place(x=8, y=17, width=140, height=27)


        # Apellidos
        self.lastName_image = PhotoImage(file="assets\\input_img.png")
        lastName_image_Label = Label(
            self,
            image=self.lastName_image,
            bg="#FFFFFF"
        )
        lastName_image_Label.place(x=293, y=242)

        self.lastName_text = Label(
            lastName_image_Label,
            text="Last name",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.lastName_text.place(x=25, y=0)

        self.lastName_icon = PhotoImage(file="assets\\name_icon.png")
        lastName_icon_Label = Label(
            lastName_image_Label,
            image=self.lastName_icon,
            bg="#3D404B"
        )
        lastName_icon_Label.place(x=159, y=15)

        self.lastName_entry = Entry(
            lastName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.lastName_entry.place(x=8, y=17, width=140, height=27)

        # Email
        self.emailName_image = PhotoImage(file="assets\\email.png")
        emailName_image_Label = Label(
            self,
            image=self.emailName_image,
            bg="#FFFFFF"
        )
        emailName_image_Label.place(x=80, y=311)

        self.emailName_text = Label(
            emailName_image_Label,
            text="Email",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.emailName_text.place(x=25, y=0)

        self.emailName_icon = PhotoImage(file="assets\\email-icon.png")
        emailName_icon_Label = Label(
            emailName_image_Label,
            image=self.emailName_icon,
            bg="#3D404B"
        )
        emailName_icon_Label.place(x=370, y=15)

        self.emailName_entry = Entry(
            emailName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.emailName_entry.place(x=8, y=17, width=354, height=27)

        # Contraseña
        self.passwordName_image = PhotoImage(file="assets\\input_img.png")
        passwordName_image_Label = Label(
            self,
            image=self.passwordName_image,
            bg="#FFFFFF"
        )
        passwordName_image_Label.place(x=80, y=380)

        self.passwordName_text = Label(
            passwordName_image_Label,
            text="Password",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.passwordName_text.place(x=25, y=0)

        self.passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
        passwordName_icon_Label = Label(
            passwordName_image_Label,
            image=self.passwordName_icon,
            bg="#3D404B"
        )
        passwordName_icon_Label.place(x=159, y=15)

        self.passwordName_entry = Entry(
            passwordName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
            show="*"
        )
        self.passwordName_entry.place(x=8, y=17, width=140, height=27)


        # Confirmar contraseña
        self.confirmar_passwordName_image = PhotoImage(file="assets\\input_img.png")
        confirmar_passwordName_image_Label = Label(
            self,
            image=self.confirmar_passwordName_image,
            bg="#FFFFFF"
        )
        confirmar_passwordName_image_Label.place(x=293, y=380)

        self.confirmar_passwordName_text = Label(
            confirmar_passwordName_image_Label,
            text="Confirm Password",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.confirmar_passwordName_text.place(x=25, y=0)

        self.confirmar_passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
        confirmar_passwordName_icon_Label = Label(
            confirmar_passwordName_image_Label,
            image=self.confirmar_passwordName_icon,
            bg="#3D404B"
        )
        confirmar_passwordName_icon_Label.place(x=159, y=15)

        self.confirmar_passwordName_entry = Entry(
            confirmar_passwordName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
            show = "*"
        )
        self.confirmar_passwordName_entry.place(x=8, y=17, width=140, height=27)

        # Pregunta clave
        self.question_image = PhotoImage(file="assets\\email.png")
        question_image_Label = Label(
            self,
            image=self.question_image,
            bg="#FFFFFF"
        )
        question_image_Label.place(x=80, y=450)

        self.question_text = Label(
            question_image_Label,
            text="Question: Where were you born?",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.question_text.place(x=25, y=0)

        self.question_icon = PhotoImage(file="assets\\name_icon.png")
        question_icon_Label = Label(
            question_image_Label,
            image=self.question_icon,
            bg="#3D404B"
        )
        question_icon_Label.place(x=370, y=15)

        self.question_entry = Entry(
            question_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.question_entry.place(x=8, y=17, width=354, height=27)



        #Submit
        self.submit_buttonImage = PhotoImage(
            file="assets/button_1.png")
        self.submit_button = Button(
            self,
            image=self.submit_buttonImage,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#272A37",
            cursor="hand2",
            bg="#FFFFFF",
            command=self.add_datos
        )
        self.submit_button .place(x=130, y=560, width=333, height=65)



        self.email = ""

        #Traduccion
        self.traducir()





    def validacion_email(self):
        query = 'SELECT email FROM datos'
        registros_db = db_consulta(query)
        resultados = registros_db.fetchall()
        self.email = self.emailName_entry.get()

        if resultados == []:


                return True
        else:
            encontrar = False
            for dato in resultados:
                if self.email == dato[0]:
                    encontrar = True

                else:
                    encontrar = False

            if encontrar == True:
                if idioma == "English":
                    messagebox.showerror(message="That email address already exists.", title="Error")
                else:
                    messagebox.showerror(message="Ese correo ya existe", title="Error")
                return False
            else:
                return True



    def validacion_password(self):
        if len(self.passwordName_entry.get()) != 0:
            if self.confirmar_passwordName_entry.get() == self.passwordName_entry.get():
                return True

            else:
                if idioma == "English":
                    messagebox.showerror(message="Passwords do not match.", title="Error")
                else:
                    messagebox.showerror(message="Las contraseñas no coinciden.", title="Error")
        else:

            if idioma == "English":
                messagebox.showerror(message="Please put a password", title="Error")
            else:
                messagebox.showerror(message="Porfavor introduzca una contraseña.", title="Error")

    def validacion_nombre(self):


        if len(self.firstName_entry.get()) == 0:
            if idioma == "English":
                messagebox.showerror(message="Please put a name", title="Error")
            else:
                messagebox.showerror(message="Porfavor introduzca su nombre.", title="Error")
        else:

            return True

    def validacion_apellidos(self):

        apellidos = self.lastName_entry.get()

        if len(apellidos) == 0:
            if idioma == "English":
                messagebox.showerror(message="Please put a lastname", title="Error")
            else:
                messagebox.showerror(message="Porfavor introduzca sus apellidos.", title="Error")
        else:

            return True

    def validacion_pregunta(self):

        pregunta = self.question_entry.get()

        if len(pregunta) == 0:
            if idioma == "English":
                messagebox.showerror(message="Please answer the question.", title="Error")
            else:
                messagebox.showerror(message="Porfavor responda la pregunta.", title="Error")
        else:

            return True






    def add_datos(self):

        query = 'INSERT INTO datos VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)'  # Consulta SQL (sin los datos)

        if self.validacion_nombre() and self.validacion_password() and self.validacion_email() and self.validacion_apellidos() and self.validacion_pregunta():
            email = self.emailName_entry.get()
            password = generate_password_hash(self.passwordName_entry.get(), 'pbkdf2:sha256:30', 45)
            idioma = "English"
            day = date.today()
            logueado = True
            limite = 2000
            strike = 0
            pregunta = self.question_entry.get()

            #Escribimos el email en un archivo de localdata para asi poder utilizarlo en otros archivos sin problema alguno
            #Si queremos buscarlo en la base de datos y hay varias ips asociadas a distintos emails habra un error y se confundira entre cuentas

            archivo = open("database\\localdata.txt", "w")
            archivo.write(email)
            archivo.close()



            #Añadimos los datos a la base de datos

            parametros = (email, self.firstName_entry.get(), self.lastName_entry.get(),password, idioma, day,logueado, limite, strike, pregunta)

            db_consulta(query, parametros)

            #Salimos y abrimos la app principal
            self.destroy()
            os.system("python app.py")





    #Traducimos
    def traducir(self):
        query = 'SELECT lg FROM datos WHERE email = ?'
        registros_db = db_consulta(query, (self.email,))
        resultados = registros_db.fetchall()

        if resultados != []:
            for dato in resultados:
                idioma = dato[0]
                if idioma == "Español":

                    self.register.config(text="Crear una cuenta")
                    self.text.config(text="¿Ya eres miembro?")
                    self.loguearse.config(text="Loguearse")
                    self.firstName_text.config(text="Nombre")
                    self.lastName_text.config(text="Apellidos")
                    self.emailName_text.config(text="Email")
                    self.passwordName_text.config(text="Contraseña")
                    self.confirmar_passwordName_text.config(text="Confirmar Contraseña")
                    self.question_text.config(text="Pregunta: ¿Donde nacistes?")

    def loguearse(self):

        self.logueo = Logueo()
        self.destroy()















