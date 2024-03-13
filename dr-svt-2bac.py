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
            ListItemWithCheckbox(text=f"Consommation de la matière organique(Partie 1)", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Consommation de la matière organique(Partie 2)", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Consommation de la matière organique(Partie 3)", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Rôle du muscle strié squelettique dans la conversion",icon="book")
        )

        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Rôle du muscle strié squelettique(Partie 2)", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Nature de l’information génétique (Partie 1)", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Nature de l’information génétique (Partie 2)", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Nature de l’information génétique (Partie 3)", icon="book")
        )

        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Nature de l’information génétique (Partie 4)", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Expression de l’information génétique (Partie 1)", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Expression de l’information génétique (Partie 2)", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Consommation de la matière organique et flux d’énergie", icon="book")
        )

        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Nature et mécanisme de l’expression du matériel génétique", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Utilisation des matières organiques et inorganiques", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Les phénomènes géologiques accompagnant la formation des chaînes de montagnes et leur relation avec la tectonique des plaques", icon="book")
        )
        self.root.ids.scroll.add_widget(
            ListItemWithCheckbox(text=f"Transformations liées à des réactions acide-base", icon="book")
        )


Test().run()