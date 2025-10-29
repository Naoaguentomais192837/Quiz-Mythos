import flet as ft

# Tela de Conquistas: usa background3.png sem logo.
# Mostra conquistas bloqueadas/desbloqueadas com base no state.

class AchievementsView(ft.View):
    def __init__(self, page, go_to, state=None):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.state = state if state is not None else {}
        self.expand = True

        background = ft.Image(src="background3.png", fit=ft.ImageFit.COVER, expand=True)

        title = ft.Text("Conquistas", size=26, weight=ft.FontWeight.BOLD)

        # definição das conquistas (id, título, descrição, threshold)
        self.achievements = [
            ("first_step", "Primeiros Passos", "Complete sua primeira pergunta", 1),
            ("genius", "Gênio Iniciante", "Acumule 10 respostas corretas", 10),
            ("nile_explorer", "Explorador do Nilo", "Responda corretamente a 15 perguntas", 15),
            ("pyramid", "Pirâmide", "Conclua 3 missões", 3)
        ]

        items = []
        correct = self.state.get("correct_answers", 0)
        answered = self.state.get("questions_answered", 0)
        first = self.state.get("first_answer", False)

        for aid, title_text, desc, threshold in self.achievements:
            unlocked = False
            if aid == "first_step":
                unlocked = bool(first)
            elif aid in ("genius",):
                unlocked = correct >= threshold
            elif aid in ("nile_explorer",):
                unlocked = correct >= threshold
            elif aid == "pyramid":
                unlocked = answered >= threshold

            icon = ft.Icon(name=ft.icons.STAR if unlocked else ft.Icons.LOCK, color="#cfa03b" if unlocked else "grey")
            badge = ft.Container(content=icon, width=48, height=48, alignment=ft.alignment.center)
            title_txt = ft.Text(title_text, weight=ft.FontWeight.BOLD)
            desc_txt = ft.Text(desc, size=12, color="black54")
            row = ft.Row([
                badge,
                ft.Column([title_txt, desc_txt], alignment=ft.MainAxisAlignment.CENTER)
            ], alignment=ft.MainAxisAlignment.START, spacing=16)
            # estilo do container
            items.append(ft.Container(content=row, padding=ft.padding.all(12), bgcolor="white70", border_radius=12))

        content = ft.Column(
            [
                ft.Row([ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS, on_click=lambda _: self.go_to("menu")), title]),
                ft.Container(height=14),
                ft.Column(items, spacing=12)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH
        )

        self.controls = [
            ft.Stack([
                ft.Container(content=background, expand=True),
                ft.Container(content=content, padding=ft.padding.only(top=40, left=16, right=16), expand=True)
            ], expand=True)
        ]
