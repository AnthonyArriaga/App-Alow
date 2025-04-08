from kivy.app import App
from kivy.core.text import layout_text
from kivy.uix.label import *
from kivy.uix.button import *
from kivy.uix.textinput import *
from kivy.uix.floatlayout import *
from kivy.core.window import *

class RootWidget(FloatLayout):
    pass

class HelloApp(App):

    def build(self):
        return RootWidget()

HelloApp().run()