from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivy.properties import StringProperty

Window.size = (400, 600)
KV = '''
MDScreen:

    MDBottomNavigation:
        panel_color: "#0a0a0a"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: "lessons"
            icon: "book-search"
            md_bg_color: (0, 0, 0, 0)  # Set alpha to 0 for transparency
            radius: [10, 15, 0, 0]

            MDScrollView:

                MDList:
                    id: scroll
<ListItemWithCheckbox>:
    IconLeftWidget:
        icon: root.icon

    RightCheckbox:
'''



class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''

class Test(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    # la liste des cours physique et chemique
    def on_start(self):
        icons = list(md_icons.keys())
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Ondes mécaniques progressives", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Ondes mécaniques périodiques", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Propagation d'une onde lumineuse", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Décroissance radioactive", icon="book")
        )

        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Noyaux, masse et énergie", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Dipôle RC", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Dipôle RL", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Oscillations libres d'un circuit RLC série", icon="book")
        )

        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Circuit RLC série en régime sinusoïdal forcé", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Ondes électromagnétiques", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Modulation d'amplitude", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Transformations lentes et transformations rapides", icon="book")
        )

        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Suivi temporel d'une transformation chimique - Vitesse de réaction", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Transformations chimiques s'effectuant dans les 2 sens", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"État d'équilibre d'un système chimique", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Transformations liées à des réactions acide-base", icon="book")
        )


Test().run()