import flet as ft # type: ignore
from viewmodel.main_viewmodel import MainViewModel  

class MainView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.view_model = MainViewModel(self)
        self.setup_ui()

    def setup_ui(self):
        self.page.title = "Tékasomba!"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.drawer = ft.NavigationDrawer(
            on_dismiss=self.view_model.handle_dismissal,
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(label="Produits", icon=ft.icons.SHOP),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(label="Mon Compte", icon_content=ft.Icon(ft.icons.ACCOUNT_CIRCLE)),
                ft.NavigationDrawerDestination(label="Aide", icon_content=ft.Icon(ft.icons.HELP)),
            ],
        )

        self.page.add(self.drawer)
        self.page.add(ft.ElevatedButton("Ouvrir le tiroir", on_click=lambda e: self.page.open(self.drawer)))
        self.view_model.show_products()