import flet as ft

# Tela de Conquistas: Mostra conquistas bloqueadas/desbloqueadas

class AchievementsView(ft.View):
    def __init__(self, page, go_to, state=None):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.state = state if state is not None else {}
        self.expand = True

        background = ft.Image(src="background3.png", fit=ft.ImageFit.COVER, expand=True)

        # Título centralizado e maior
        title = ft.Text("Conquistas", size=28, weight=ft.FontWeight.BOLD, color="black")

        # definição das conquistas (id, título, descrição, threshold)
        self.achievements = [
            ("first_step", "Primeiros Passos", "Complete sua primeira pergunta.", 1),
            ("genius", "Gênio Iniciante", "Acumule 10 respostas corretas.", 10),
            ("nile_explorer", "Explorador do Nilo", "Responda corretamente a 15 perguntas.", 15),
            ("pyramid", "Pirâmide Completa", "Responda a todas as 3 perguntas do quiz.", 3)
        ]

        items = []
        correct = self.state.get("correct_answers", 0)
        answered = self.state.get("questions_answered", 0)
        first = self.state.get("first_answer", False)

        for aid, title_text, desc, threshold in self.achievements:
            unlocked = False
            
            if aid == "first_step":
                unlocked = bool(first)
            elif aid in ("genius", "nile_explorer"):
                unlocked = correct >= threshold
            elif aid == "pyramid":
                unlocked = answered >= threshold 
            
            icon_color = "#cfa03b" if unlocked else ft.Colors.BLUE_GREY_200 
            card_bgcolor = "#FFD700" if unlocked else ft.Colors.GREY_200 

            icon = ft.Icon(name=ft.Icons.STAR if unlocked else ft.Icons.LOCK, color=icon_color, size=30)
            
            icon_container = ft.Container(
                content=icon,
                width=50,
                height=50,
                border_radius=25,
                bgcolor=ft.Colors.WHITE70 if unlocked else ft.Colors.BLUE_GREY_100,
                alignment=ft.alignment.center
            )

            title_txt = ft.Text(title_text, weight=ft.FontWeight.BOLD, color="black", size=16)
            
            # indicador de progresso
            if unlocked:
                 progress_text = ft.Text("Desbloqueada!", size=12, color=ft.Colors.BLACK54, weight=ft.FontWeight.W_600)
            else:
                 progress_text = ft.Text(f"Progresso: {answered}/{threshold}" if aid == "pyramid" else f"Progresso: {correct}/{threshold}", size=12, color=ft.Colors.BLACK54)
            
            # progresso
            text_column = ft.Column(
                [title_txt, progress_text], 
                alignment=ft.MainAxisAlignment.CENTER, 
                spacing=2, 
                expand=True
            )


            row_content = ft.Row([
                icon_container,
                text_column
            ], alignment=ft.MainAxisAlignment.START, spacing=16)
            
            card_item = ft.Card(
                content=ft.Container(
                    content=row_content,
                    padding=ft.padding.all(15),
                    bgcolor=card_bgcolor,
                    border_radius=12
                ),
                elevation=5, 
                margin=ft.margin.symmetric(vertical=6) 
            )
            items.append(card_item)

        # BOTÃO DE VOLTAR E TÍTULO
        top_row = ft.Row(
            [
                ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS, on_click=lambda _: self.go_to("menu"), icon_color="black"),
                ft.Container(content=title, alignment=ft.alignment.center_left, expand=True)
            ],
            alignment=ft.MainAxisAlignment.START
        )

        content = ft.Column(
            [
                top_row,
                ft.Container(height=14),
                ft.ListView(items, spacing=0, expand=True) # Usamos ListView para permitir rolagem
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            expand=True
        )

        self.controls = [
            ft.Stack([
                ft.Container(content=background, expand=True),
                ft.Container(content=content, padding=ft.padding.only(top=30, left=16, right=16, bottom=16), expand=True)
            ], expand=True)
        ]