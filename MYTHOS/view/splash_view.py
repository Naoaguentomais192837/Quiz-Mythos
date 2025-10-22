import flet as ft
import asyncio

# Mostra o logotipo do Mythos antes de iniciar o aplicativo.
# Após alguns segundos, redireciona automaticamente para
# a tela inicial ("StartView").

class SplashView(ft.View):
    def __init__(self, page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.expand = True

#Define o background e a logo

        background = ft.Image(src="background1.png", fit=ft.ImageFit.COVER, expand=True)
        logo = ft.Image(src="anubis_logo.png", width=220, height=220)

#centraliza

        content = ft.Column(
            [logo],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

#adiciona os elementos na tela

        self.controls = [
            ft.Stack([
                ft.Container(content=background, expand=True),
                ft.Container(content=content, alignment=ft.alignment.center, expand=True)
            ], expand=True)
        ]

        page.run_task(self._delayed_nav)

    async def _delayed_nav(self):
        await asyncio.sleep(2)
        self.go_to("start")


