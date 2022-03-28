
import kivy.app as app
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (414, 736)

class Main(Screen):
    Username = 'Max'
    Currency = '$'
    Perriod = 'March'
    Balance = 50000
    StrBalance = str(Balance)

class Costs(Screen):
    pass

class MoneyCounterApp(app.App):
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main(name='Main'))
        sm.add_widget(Costs(name='Costs'))
        return sm



if __name__ == "__main__":
    MoneyCounterApp().run()
