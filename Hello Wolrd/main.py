from kivy.app import App
from kivy.core.text import layout_text
from kivy.uix.label import *
from kivy.uix.button import *
from kivy.uix.textinput import *
from kivy.uix.floatlayout import *
from kivy.core.window import *

class hello_world(App):

    def click(self):
        print("Clickeado")

    def build(self):

        layout = FloatLayout()
        lb = Label()
        lb.x = 250
        lb.y = 400
        lb.size_hint = None, None
        lb.height = 100
        lb.width = 100
        lb.text="Hello Wolrd"
        lb.italic=True
        lb.font_size=50
        bt = Button()
        bt.x = 250
        bt.y = 50
        bt.size_hint = None, None
        bt.height = 50
        bt.width = 100
        bt.text="Clickeame"
        dato = TextInput()
        dato.x = 200
        dato.y = 150
        dato.size_hint = None, None
        dato.height = 250
        dato.width = 200
        layout.add_widget(lb)
        layout.add_widget(bt)
        layout.add_widget(dato)
        bt.on_press = self.click

        return layout

Window.size= 600, 600
hello_world().run()
