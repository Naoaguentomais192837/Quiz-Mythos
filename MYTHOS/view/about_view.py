import flet as ft

# Tela Sobre: usa background2.png, logo e texto mais elaborado.

class AboutView(ft.View):
    def __init__(self, page, go_to, state=None):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.state = state if state is not None else {}
        self.expand = True

        background = ft.Image(src="background2.png", fit=ft.ImageFit.COVER, expand=True)
        logo = ft.Image(src="anubis_logo.png", width=110, height=110)

        headline = ft.Text("Sobre o Mythos", size=24, weight=ft.FontWeight.BOLD)
        body = ft.Text(
            "O Mythos é um aplicativo interativo dedicado a celebrar e ensinar a mitologia do Antigo Egito. "
            "Projetado tanto para entusiastas quanto para curiosos, o aplicativo combina um design elegante inspirado "
            "nos símbolos egípcios com um formato de quiz dinâmico que testa e amplia seu conhecimento.\n\n"
            "Cada pergunta foi cuidadosamente elaborada por pesquisadores e apaixonados pela cultura egípcia, "
            "abrangendo deuses, lendas, símbolos e curiosidades históricas. Responda perguntas, desbloqueie conquistas "
            "e embarque em uma jornada educativa que revela a riqueza e o mistério das areias do Nilo.\n\n"
            "Desenvolvido com atenção ao detalhe visual e à experiência do usuário, o Mythos busca tornar o aprendizado "
            "divertido, acessível e memorável. Boa sorte — e que os deuses sorriam para você!",
            size=14
        )

        content = ft.Column(
            [
                ft.Row([ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS, on_click=lambda _: self.go_to("menu")), logo]),
                ft.Container(height=8),
                headline,
                ft.Container(height=10),
                ft.Container(content=body, padding=ft.padding.all(8))
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.controls = [
            ft.Stack([
                ft.Container(content=background, expand=True),
                ft.Container(content=content, padding=ft.padding.only(top=30, left=18, right=18), expand=True)
            ], expand=True)
        ]
