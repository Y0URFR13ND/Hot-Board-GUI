from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.properties import ObjectProperty



class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Hot Board"
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        super().__init__(**kwargs)



MainApp().run()

'''
Button:
        id: 'test_btn'
        text: "Test Button 1"
        on_press: self.background_color = 0,0,0,1
        on_release: self.background_color = 0.95, 0.95, 0.95, 1
        
                Button:
                    text: 'G1'
                Button:
                    text: 'G2'
                Button:
                    text: 'G3'
                Button:
                    text: 'G4'
                Button:
                    text: 'G5'
                Button:
                    text: 'G6'
                Button:
                    text: 'G7'
                Button:
                    text: 'G8'
                Button:
                    text: 'G9'
                Button:
                    text: 'G10'
                Button:
                    text: 'G11'
                Button:
                    text: 'G12'
                    
'''