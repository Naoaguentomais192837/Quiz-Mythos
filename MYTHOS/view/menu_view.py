import flet as ft

class MenuView(ft.View):
    def __init__(self, page, go_to, state=None):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.state = state if state is not None else {}
        self.expand = True

        background = ft.Image(src="background2.png", fit=ft.ImageFit.COVER, expand=True)
        logo = ft.Image(src="anubis_logo.png", width=120, height=120)

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

        # ÍCONE DE INFO 
        info_icon_button = ft.Container(
            content=ft.IconButton(
                icon=ft.Icons.INFO_OUTLINE,
                icon_color="white", # Cor do ícone
                on_click=lambda _: self.go_to("about"),
                tooltip="Sobre o aplicativo"
            ),
            width=40, 
            height=40,
            border_radius=20, 
            bgcolor="#002B5B", 
            alignment=ft.alignment.center
        )

        top_row = ft.Row(
            [
                ft.Container(width=48), 
                ft.Text("", expand=True), 
                info_icon_button 
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