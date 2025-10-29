import flet as ft

# Esse é o código da tela do sobre

class AboutView(ft.View):
    def __init__(self, page, go_to, state=None):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.state = state if state is not None else {}
        self.expand = True

        background = ft.Image(src="background2.png", fit=ft.ImageFit.COVER, expand=True)
        logo = ft.Image(src="anubis_logo.png", width=110, height=110)

        # Título principal
        headline = ft.Text("Sobre o Mythos", size=24, weight=ft.FontWeight.BOLD, color="white")

        # Conteúdo do texto
        body = ft.Text(
            "O Mythos é um aplicativo interativo dedicado a celebrar e ensinar a mitologia do Antigo Egito. "
            "Projetado tanto para entusiastas quanto para curiosos, o aplicativo combina um design elegante inspirado "
            "nos símbolos egípcios com um formato de quiz dinâmico que testa e amplia seu conhecimento.\n\n"
            "Cada pergunta foi cuidadosamente elaborada por pesquisadores e apaixonados pela cultura egípcia, "
            "abrangendo deuses, lendas, símbolos e curiosidades históricas. Responda perguntas, desbloqueie conquistas "
            "e embarque em uma jornada educativa que revela a riqueza e o mistério das areias do Nilo.\n\n"
            "Desenvolvido com atenção ao detalhe visual e à experiência do usuário, o Mythos busca tornar o aprendizado "
            "divertido, acessível e memorável. Boa sorte — e que os deuses sorriam para você!",
            size=14,
            color="white" 
        )

        content_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        headline,
                        ft.Container(height=10),
                        body
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    spacing=0
                ),
                padding=ft.padding.all(20),
                bgcolor="#002B5B", # Cor azul escura dos botões
                border_radius=15, # Bordas arredondadas
            ),
            elevation=10 
        )

        # Botão de voltar e Logo
        top_row = ft.Row(
            [
                ft.IconButton(
                    icon=ft.Icons.ARROW_BACK_IOS, 
                    on_click=lambda _: self.go_to("menu"),
                    icon_color="black", # Botão preto para visibilidade no topo claro
                ),
                ft.Container(width=40, expand=True),
                ft.Container(content=logo, alignment=ft.alignment.center)
            ],
            alignment=ft.MainAxisAlignment.START,
        )

        final_content = ft.Column(
            [
                top_row,
                ft.Container(height=20),
                content_card
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            expand=True
        )

        self.controls = [
            ft.Stack([
                ft.Container(content=background, expand=True),
                ft.Container(
                    content=final_content, 
                    padding=ft.padding.only(top=30, left=25, right=25), 
                    expand=True
                )
            ], expand=True)
        ]