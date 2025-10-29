import flet as ft

# Contém botões para iniciar o quiz e ver as pontuações (conquistas).
# Adicionado ícone de informação no topo que leva para AboutView.

class MenuView(ft.View):
    def __init__(self, page, go_to, state=None):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.state = state if state is not None else {}
        self.expand = True

        # Fundo e logo
        background = ft.Image(src="background2.png", fit=ft.ImageFit.COVER, expand=True)
        logo = ft.Image(src="anubis_logo.png", width=120, height=120)

        # botão para iniciar quiz
        play_button = ft.ElevatedButton(
            text="Iniciar Quiz",
            icon=ft.Icons.PLAY_ARROW,
            bgcolor="#002B5B",
            color="white",
            width=200,
            height=50,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
            on_click=lambda _: self.go_to("quiz")
        )

        # botão para ver conquistas
        score_button = ft.ElevatedButton(
            text="Ver Conquistas",
            icon=ft.Icons.LIST,
            bgcolor="#002B5B",
            color="white",
            width=200,
            height=50,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
            on_click=lambda _: self.go_to("achievements")
        )

        # topo com ícone de info
        top_row = ft.Row(
            [
                ft.Container(width=48),  # espaço à esquerda
                ft.Text("", expand=True),
                ft.IconButton(icon=ft.Icons.INFO_OUTLINE, on_click=lambda _: self.go_to("about"))
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        content = ft.Column(
            [top_row, logo, ft.Container(height=20), play_button, score_button],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.controls = [
            ft.Stack([
                ft.Container(content=background, expand=True),
                ft.Container(content=content, alignment=ft.alignment.center, expand=True)
            ], expand=True)
        ]
