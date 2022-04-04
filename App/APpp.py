import os
from posixpath import dirname
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
import kivy.app as app
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (414, 736)

Builder.load_file(os.path.join( dirname(__file__), 'Main.kv'))
Builder.load_file(os.path.join( dirname(__file__), 'AllTransactions.kv'))
Builder.load_file(os.path.join( dirname(__file__), 'AddTransaction.kv'))

class Data():
    pass

class Main(Screen, Data):
    Username = 'Max'
    Currency = '$'
    Perriod = 'March'
    Balance = 50000
    StrBalance = str(Balance)

class Costs(Screen, Data):
    pass

class AllTransactions(Screen, Data):
    pass

class AddTransaction(Screen , Data):
    pass

class MoneyCounterApp(app.App):
    
    def build(self):
        sm = ScreenManager()
        #sm.add_widget(Main(name='Main'))
        #sm.add_widget(AllTransactions(name='AllTransactions'))
        sm.add_widget(AddTransaction(name='AddTransaction'))
        return sm



if __name__ == "__main__":
    MoneyCounterApp().run()
