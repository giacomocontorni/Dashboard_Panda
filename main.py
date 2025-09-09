from kivy.config import Config
Config.set('kivy', 'video', 'ffpyplayer')  # Deve venire PRIMA degli import di Kivy
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '400')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import os

# Forziamo il caricamento del file .kv
Builder.load_file(os.path.join(os.path.dirname(__file__), 'main.kv'))

class SplashScreen(Screen):
    pass

class ToolBar(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='pagina1'))
        sm.add_widget(ToolBar(name='pagina2'))
        sm.current = 'pagina1'  # schermata iniziale
        return sm

if __name__ == '__main__':
    MyApp().run()
