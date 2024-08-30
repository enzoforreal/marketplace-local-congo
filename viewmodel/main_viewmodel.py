import flet as ft # type: ignore
from model.product import products  

class MainViewModel:
    def __init__(self, view):
        self.view = view

    def handle_dismissal(self, e):
        self.view.page.add(ft.Text("Tiroir fermé"))

    def show_products(self):
        self.view.page.clean()
        self.view.page.add(ft.AppBar(title=ft.Text("Produits"), bgcolor=ft.colors.BLUE_600))
        
        for product in products:
            self.view.page.add(
                ft.Column(
                    [
                        ft.Text(product['name'], size=20),
                        ft.Text(product['description']),
                        ft.Text(f"Prix: {product['price']} XAF"),
                        ft.ElevatedButton(
                            text="Acheter",
                            on_click=lambda e, product_id=product['id']: self.purchase(product_id, '0771234567')
                        ),
                        ft.Divider()
                    ]
                )
            )

    def purchase(self, product_id, phone_number):
        # Logique d'achat ici
        pass