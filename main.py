import flet as ft  # type: ignore
from model.product import products
from momo_payment_lib import process_payment  

def main(page: ft.Page):
    page.title = "Tékasomba!"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_dismissal(e):
        page.add(ft.Text("Tiroir fermé"))

    # Créer le tiroir de navigation
    drawer = ft.NavigationDrawer(
        on_dismiss=handle_dismissal,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Produits",
                icon=ft.icons.SHOP,
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                label="Mon Compte",
                icon_content=ft.Icon(ft.icons.ACCOUNT_CIRCLE),
            ),
            ft.NavigationDrawerDestination(
                label="Aide",
                icon_content=ft.Icon(ft.icons.HELP),
            ),
        ],
    )

    # Ajouter le tiroir de navigation à la page
    page.add(drawer)

    # Ajouter un bouton pour ouvrir le tiroir
    open_drawer_button = ft.ElevatedButton("Ouvrir le tiroir", on_click=lambda e: page.open(drawer))
    page.add(open_drawer_button)

    # Gérer les clics sur les destinations du tiroir
    def on_destination_click(e):
        if e.control.label == "Produits":
            show_products()
        elif e.control.label == "Mon Compte":
            show_account()
        elif e.control.label == "Aide":
            show_help()

    # Associer la fonction de clic aux destinations
    for destination in drawer.controls:
        if isinstance(destination, ft.NavigationDrawerDestination):
            destination.on_click = on_destination_click  # Gérer les clics ici

    # Fonction pour afficher les produits
    def show_products():
        page.clean()  # Nettoyer la page avant de réafficher les produits
        page.add(open_drawer_button)  # Réajouter le bouton pour ouvrir le tiroir
        page.add(ft.AppBar(title=ft.Text("Produits"), bgcolor=ft.colors.BLUE_600))
        
        # Affichage des produits
        for product in products:
            page.add(
                ft.Column(
                    [
                        ft.Text(product['name'], size=20),
                        ft.Text(product['description']),
                        ft.Text(f"Prix: {product['price']} XAF"),
                        ft.ElevatedButton(
                            text="Acheter",
                            on_click=lambda e, product_id=product['id']: purchase(product_id, '0771234567')
                        ),
                        ft.Divider()
                    ]
                )
            )

    # Fonction pour afficher la section "Mon Compte"
    def show_account():
        page.clean()
        page.add(open_drawer_button)  # Réajouter le bouton pour ouvrir le tiroir
        page.add(ft.AppBar(title=ft.Text("Mon Compte"), bgcolor=ft.colors.BLUE_600))
        page.add(ft.Text("Détails de votre compte."))

    # Fonction pour afficher la section "Aide"
    def show_help():
        page.clean()
        page.add(open_drawer_button)  # Réajouter le bouton pour ouvrir le tiroir
        page.add(ft.AppBar(title=ft.Text("Aide"), bgcolor=ft.colors.BLUE_600))
        page.add(ft.Text("Page d'aide et FAQ."))

    # Fonction de traitement d'achat
    def purchase(product_id, phone_number):
        amount = next((product['price'] for product in products if product['id'] == product_id), None)
        if amount is not None:
            success = process_payment(amount, phone_number)  # Utilisez votre librairie
            if success:
                page.add(ft.Text("Achat réussi!", color=ft.colors.GREEN))
            else:
                page.add(ft.Text("Échec de l'achat.", color=ft.colors.RED))
        else:
            page.add(ft.Text("Produit non trouvé.", color=ft.colors.RED))

    show_products()  # Afficher la liste des produits par défaut

ft.app(main)