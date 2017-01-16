
import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.button import Label

class HelloKivyApp(App):
 
    # This returns the content we want in the window
    def build(self):
        return Label()
 
hello_kivy = HelloKivyApp()
hello_kivy.run()