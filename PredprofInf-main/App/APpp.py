from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition 
from kivy.core.window import Window
import os
from kivy.properties import StringProperty

Window.size = (414, 736)

class All(Screen):
    month = ' Марта'
    date = '9'
    def toTheMain(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Main'

class Main(Screen):
    Username = 'Max'
    Currency = '$'
    Perriod = 'March'
    Balance = 50000
    StrBalance = str(Balance)
    cost = '-50 р'
    operation = 'Бутылка молока'
    space = '                                     ' 
    def toTheAll(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'All'
    def toTheOpMenu(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'OpMenu'

class Costs(Screen):
    pass

class OpMenu(Screen):
    cost = '-50 р'
    operation = 'Бутылка молока'
    space = '                                     ' 
    def toTheMain(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Main'
        

class Test(Screen):
    pass

class MoneyCounterApp(App):
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main(name='Main'))
        sm.add_widget(OpMenu(name='OpMenu'))
        sm.add_widget(Test(name='Test'))
        sm.add_widget(All(name='All'))
        sm.add_widget(Costs(name='Costs'))
        return sm



if __name__ == "__main__":
    MoneyCounterApp().run()
