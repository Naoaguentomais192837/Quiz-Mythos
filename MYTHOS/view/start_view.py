import flet as ft

# Mostra o logotipo e um botão para iniciar o aplicativo.
# Ao clicar, o usuário é levado ao menu principal.

class StartView(ft.View):
    def __init__(self, page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.expand = True

        #backgorund e logo

        background = ft.Image(src="background2.png", fit=ft.ImageFit.COVER, expand=True)
        logo = ft.Image(src="anubis_logo.png", width=150, height=150)

        #botão para o menu

        start_button = ft.ElevatedButton(
            text="Iniciar",
            bgcolor="#002B5B",
            color="white",
            width=200,
            height=50,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
            on_click=lambda _: go_to("menu")
        )

        #centraliza

        content = ft.Column(
            [logo, ft.Container(height=20), start_button],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        #monta a estrutura da tela

        self.controls = [
            ft.Stack([
                ft.Container(content=background, expand=True),
                ft.Container(content=content, alignment=ft.alignment.center, expand=True)
            ], expand=True)
        ]



