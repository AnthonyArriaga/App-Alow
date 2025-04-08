import sqlite3
from kivy.app import App
from kivy.core.text import layout_text
from kivy.uix.label import *
from kivy.uix.button import *
from kivy.uix.textinput import *
from kivy.uix.floatlayout import *
from kivy.core.window import *
from kivy.uix.screenmanager import *
from kivy.clock import *
from kivy.uix.boxlayout import *


class Inicio(App):

    def build(self):

        ven = ScreenManager()
        ven.add_widget(Vent_Inicio(name="inicio"))
        ven.add_widget(Login(name="login"))
        ven.add_widget(MainScreenAdmin(name="mainadmin"))
        ven.add_widget(MainScreenUsuario(name="mainusuario"))
        return ven

class Vent_Inicio(Screen):

    def logeo(self):
        self.manager.current = "login"

class Login (Screen):

    def Val_Usuario(self):

        usuario = self.ids.usuario.text
        contrasena = self.ids.contrasena.text

        try:

            conn = sqlite3.connect(r'C:\Users\alow.29\Documents\App\.venv1\Source\Data_Bases\usuarios.db')
            print("Conexion exitosa a la base de datos.")
            cursor = conn.cursor()

            cursor.execute('''
                    SELECT * FROM Usuarios WHERE Usuario = ? AND Contra = ?
                    ''', (usuario, contrasena))

            usuario_encontrado = cursor.fetchone()

            if usuario_encontrado:

                print("✅ Usuario y contraseña correctos")
                cursor.execute("SELECT Tipo FROM Usuarios WHERE Usuario = ? AND Contra = ?", (usuario, contrasena))
                Tipo = cursor.fetchone()

                if(Tipo[0] == 'Administrador'):
                    self.manager.current = "mainadmin"

                if(Tipo[0] == 'Usuario'):
                    self.manager.current = "mainusuario"

                else:
                    self.show_toast("❌ Error de usuario.")

            else:
                self.show_toast("❌ Usuario o contraseña incorrectos")

            conn.close()

        except sqlite3.Error as e:

            print("Error al conectar a la base de datos.")

    def show_toast(self, message):
        toast = Label(text=message, color=(1, 0, 0, 1), size_hint=(None, None), size=(300, 50))
        toast.pos = (self.center_x - toast.width // 2, self.center_y - toast.height // 2)
        self.add_widget(toast)
        Clock.schedule_once(lambda dt: self.remove_widget(toast), 5)

class MainScreenAdmin(Screen):

    def cerrar_ses(self):
        self.manager.current = "login"

class MainScreenUsuario(Screen):

    def cerrar_ses(self):
        self.manager.current = "login"

Inicio().run()