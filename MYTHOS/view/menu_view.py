import flet as ft

#Contém botões para iniciar o quiz e ver as pontuações.
#Cada botão redireciona para uma funcionalidade específica.

class MenuView(ft.View):
    def __init__(self, page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.expand = True
 
        #Fundo e logo

        background = ft.Image(src="background2.png", fit=ft.ImageFit.COVER, expand=True)
        logo = ft.Image(src="anubis_logo.png", width=120, height=120)

        #botão para iniciar quiz

        play_button = ft.ElevatedButton(
            text="Iniciar Quiz",
            icon=ft.Icons.PLAY_ARROW,
            bgcolor="#002B5B",
            color="white",
            width=200,
            height=50,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
            on_click=lambda _: print("Iniciar Quiz")
        )

        #botão para ver pontuações

        score_button = ft.ElevatedButton(
            text="Ver Pontuações",
            icon=ft.Icons.LIST,
            bgcolor="#002B5B",
            color="white",
            width=200,
            height=50,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
            on_click=lambda _: print("Ver Pontuações")
        )

        content = ft.Column(
            [logo, ft.Container(height=20), play_button, score_button],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.controls = [
            ft.Stack([
                ft.Container(content=background, expand=True),
                ft.Container(content=content, alignment=ft.alignment.center, expand=True)
            ], expand=True)
        ]


