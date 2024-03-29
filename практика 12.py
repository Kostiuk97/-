from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    def __init__(self, name="main"):
        super().__init__(name=name)
        layout = GridLayout(cols=2)
        
        btn1 = Button(text="Go to Screen 1", on_press=self.switch_to_screen1)
        btn2 = Button(text="Go to Screen 2", on_press=self.switch_to_screen2)
        btn3 = Button(text="Go to Screen 3", on_press=self.switch_to_screen3)
        btn4 = Button(text="Go to Screen 4", on_press=self.switch_to_screen4)
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        
        self.add_widget(layout)

    def switch_to_screen1(self, instance):
        self.manager.current = 'screen1'

    def switch_to_screen2(self, instance):
        self.manager.current = 'screen2'

    def switch_to_screen3(self, instance):
        self.manager.current = 'screen3'

    def switch_to_screen4(self, instance):
        self.manager.current = 'screen4'

class OtherScreen1(Screen):
    def __init__(self, name="first"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical') 
        back_btn = Button(text="Back", on_press=self.switch_back)
        input_text = TextInput()
        self.txt = Label(text="This is TEXT")
        layout.add_widget(self.txt)  
        layout.add_widget(back_btn) 
        layout.add_widget(input_text)
        self.add_widget(layout)

    def switch_back(self, instance):
        self.manager.current = 'main'
        
class OtherScreen2(Screen):
    def __init__(self, name="second"):
        super().__init__(name=name)
        layout = BoxLayout()
        back_btn = Button(text="Back", on_press=self.switch_back)
        slider = Slider(min=0, max=100, value=50)
        progress_bar = ProgressBar(max=100)
        layout.add_widget(back_btn)
        layout.add_widget(slider)
        layout.add_widget(progress_bar)
        self.add_widget(layout)

    def switch_back(self, instance):
        self.manager.current = 'main'
        
class OtherScreen3(Screen):
    def __init__(self, name="third"):
        super().__init__(name=name)
        layout = BoxLayout()
        back_btn = Button(text="Back", on_press=self.switch_back)
        check_box = CheckBox()
        switch = Switch()
        layout.add_widget(switch)
        layout.add_widget(check_box)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def switch_back(self, instance):
        self.manager.current = 'main'
        
class OtherScreen4(Screen):
    def __init__(self, name="forth"):
        super().__init__(name=name)
        layout = BoxLayout()
        scroll_view = ScrollView()
        content = GridLayout(cols=1, spacing=10, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))
        for i in range(50):
            label = Label(text="Label {}".format(i+1))
            content.add_widget(label)
        scroll_view.add_widget(content)
        back_btn = Button(text="Back", on_press=self.switch_back)
        toggle_button = ToggleButton(text='Off', group='toggles', state='normal')
        layout.add_widget(toggle_button)
        layout.add_widget(back_btn)
        layout.add_widget(scroll_view)
        self.add_widget(layout)

    def switch_back(self, instance):
        self.manager.current = 'main'

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        main_screen = MainScreen()
        screen1 = OtherScreen1('screen1')
        screen2 = OtherScreen2('screen2')
        screen3 = OtherScreen3('screen3')
        screen4 = OtherScreen4('screen4')

        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(screen1)
        screen_manager.add_widget(screen2)
        screen_manager.add_widget(screen3)
        screen_manager.add_widget(screen4)

        return screen_manager

MyApp().run()