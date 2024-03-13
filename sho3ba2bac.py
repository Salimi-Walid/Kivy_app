from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.properties import DictProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRaisedButton
import subprocess
Window.size = (400, 600)
KV = '''

MDScreen:

    MDBottomNavigation:
        panel_color:"#027efa"
        MDBottomNavigationItem:
            name:'screen 1'
            text:"lessons"
            icon:"book-search"
            md_bg_color: "#f5f6f7"
            MDGridLayout:
                cols: 2
                spacing: "10dp"
                padding: "10dp"
                pos_hint: {"center_x": 0.6, "center_y": 0.3}
# les carde dyal les cours
                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message("Card Clicked")
                    Image:
                        source: "image photochop\$.png"

                    MDLabel:
                        text: "Mathématiques"

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message2("Card Clicked")
                    Image:
                        source: "your_image_path2.png"

                    MDLabel:
                        text: "S.V.T"

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message3("Card Clicked")

                    Image:
                        source: "your_image_path3.png"

                    MDLabel:
                        text: "Physique et chimie"

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "140dp", "180dp"
                    on_release: app.show_message4("Card Clicked")

                    Image:
                        source: "your_image_path4.png"

                    MDLabel:
                        text: "Philosophie"
# la fin dyal card cours



    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "Najeh"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#027efa"
                    specific_text_color: "#f5f6f7"
                    left_action_items: [["arrow-left-circle", lambda x:app.go_back()]]
                    right_action_items: [["magnify", lambda x: app.on_search_icon_press(x),"sherch"]]

'''
class Example(MDApp):
    data = DictProperty()

    def build(self):
        theme_cls = ThemeManager
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"


        return Builder.load_string(KV)

    def go_back(self):
        print("dd")
        current_index = self.root.ids.screen_manager.screen_names.index(self.root.current)


        if current_index > 0:

            self.root.current = self.root.ids.screen_manager.screen_names[current_index - 1]
        else:
            self.stop()
    def show_message3(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "drph.py"])
    def show_message2(self, text):
        print("Icon Button Clicked: {button_text}")
        subprocess.Popen(["python", "dr-svt-2bac.py"])
Example().run()