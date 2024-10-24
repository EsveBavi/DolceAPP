import flet as ft
import os

def main(page: ft.Page):
    page.title = "Dolce Helato - Inicio de sesión"
    page.padding = 0
    page.bgcolor = ft.colors.WHITE
    
    # Ruta correcta de la imagen
    image_path = os.path.join("img", "logo.png")
    
    # Importar la fuente Albert Sans usando CSS
    page.on_load = lambda _: page.add(ft.Text(
        value="",
        style=ft.TextStyle(
            font_family="Albert Sans",
            font_url="https://fonts.googleapis.com/css2?family=Albert+Sans:ital,wght@0,100..900;1,100..900&display=swap"
        )
    ))
    
    def login_click(e):
        if username.value == "admin" and password.value == "admin":
            page.go("/admin")
        else:
             dialog = ft.AlertDialog(
            title=ft.Text("Error"),
            content=ft.Text("Credencial incorrecta")
             )
             page.overlay.append(dialog)
             dialog.open = True
             page.update()
    
    logo = ft.Container(
        content=ft.Image(src=image_path),
        width=100,
        height=100,
        border_radius=50,
        bgcolor=ft.colors.BLACK,
    )
    
    title = ft.Column([
        ft.Text(
            "Inicio de sesión",
            size=24,
            color="#C25B56",
            style=ft.TextStyle(
                font_family="Albert Sans",
                weight=ft.FontWeight.BOLD
            )
        ),
        ft.Container(
            content=ft.Divider(color="#D9BFA7", height=1),
            width=200
        )
    ])
    
    username = ft.TextField(
        label="USUARIO O CORREO:",
        border_color="#D9BFA7",
        focused_border_color="#D9BFA7",
        height=40,
    )
    
    password = ft.TextField(
        label="CONTRASEÑA:",
        password=True,
        can_reveal_password=True,
        border_color="#D9BFA7",
        focused_border_color="#D9BFA7",
        height=40,
    )
    
    def go_to_register(e):
        page.go("/register")
    
    def go_to_password_recovery(e):
        page.go("/recover-password")
    
    forgot_password = ft.Text(
        "¿Olvidó su contraseña? ",
        size=12,
        color="#000000",
    )
    forgot_password_link = ft.TextButton(
        text="Click aquí",
        style=ft.ButtonStyle(
            color="#4A9586",
            padding=0,
        ),
        on_click=go_to_password_recovery
    )
    
    login_button = ft.ElevatedButton(
        text="INGRESAR",
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor="#DDA965",
            shape=ft.RoundedRectangleBorder(radius=20),
        ),
        width=200,
        on_click=login_click,
    )
    
    login_button.style.font_style = ft.TextStyle(
        weight=ft.FontWeight.BOLD,
        font_family="Albert Sans"
    )
    
    register_text = ft.Text(
        "¿No tiene cuenta? ",
        size=12,
        color="#000000",
    )
    register_link = ft.TextButton(
        text="Registrarse",
        style=ft.ButtonStyle(
            color="#C25B56",
            padding=0,
        ),
        on_click=go_to_register
    )
    
    centered_container = ft.Container(
        content=ft.Column([
            logo,
            ft.Container(height=20),
            title,
            ft.Container(height=20),
            username,
            ft.Container(height=10),
            password,
            ft.Container(height=20),
            ft.Row([forgot_password, forgot_password_link], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=20),
            login_button,
            ft.Container(height=20),
            ft.Row([register_text, register_link], alignment=ft.MainAxisAlignment.CENTER),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        expand=True,
        alignment=ft.alignment.center
    )
    
    page.add(centered_container)
    
    def page_resize(e):
        centered_container.width = page.width
        centered_container.height = page.height
        page.update()
    
    page_resize = page_resize

    def admin_page(page: ft.Page):
        return ft.View(
            "/admin",
            [
                ft.AppBar(title=ft.Text("Página de Administrador")),
                ft.Text("Bienvenido a la página de administrador")
            ]
        )

    def register_page(page: ft.Page):
        return ft.View(
            "/register",
            [
                ft.AppBar(title=ft.Text("Registro")),
                ft.Text("Página de registro")
            ]
        )

    def password_recovery_page(page: ft.Page):
        return ft.View(
            "/recover-password",
            [
                ft.AppBar(title=ft.Text("Recuperar Contraseña")),
                ft.Text("Página de recuperación de contraseña")
            ]
        )

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        centered_container
                    ]
                )
            )
        elif page.route == "/admin":
            page.views.append(admin_page(page))
        elif page.route == "/register":
            page.views.append(register_page(page))
        elif page.route == "/recover-password":
            page.views.append(password_recovery_page(page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)