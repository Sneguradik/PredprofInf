import kivy.app as app
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout as gl
from kivy.uix.label import Label

Window.size = (414, 736)

class Main(Screen):
    balance = 100
    
    def get_balance(self):
        return self.balance 
        
    def ChangeWindow(self,*args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Costs'

class Costs(Screen):
    pass

class MoneyCounterApp(app.App):
    
    def callback(self, instance):
        print('The button <%s> is being pressed' % instance.text)


    def build(self):
        btn1 = Button(text='Hello world 1')
        btn1.bind(on_press = self.callback)
        btn2 = Button(text='Hello world 2')
        btn2.bind(on_press = self.callback)
        buts = BoxLayout()
        buts.add_widget(btn1)
        buts.add_widget(btn2)
        return buts
    
    
    #def build(self):
        #mybut = Button(text = "hello", font_size = 30, background_color = "yellow", on_press = self.click)
        #sm = ScreenManager()
        #sm.add_widget(Main(name='Main'))
        #sm.add_widget(Costs(name='Costs'))
        #sm.add_widget(mybut)
        #return sm


    #def bebra(self):
        #buts = BoxLayout()
        #grid = gl(cols = 1)

        #mybut = Button(text = "hello", font_size = 30, background_color = "yellow", on_press = self.click)
        #mybut2 = Button(text = "bye", font_size = 30, background_color = "red")
        #self.label = Label(text = "XD", font_size = 30)
        #buts.add_widget(mybut)
        #buts.add_widget(mybut2)
        #grid.add_widget(buts)
        #grid.add_widget(self.label)

if __name__ == "__main__":
    MoneyCounterApp().run()
