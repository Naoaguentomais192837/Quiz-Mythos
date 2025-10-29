import flet as ft
import asyncio

# Tela do Quiz: usa background2.png e anubis_logo.png
# Corrigido bug de cores — agora reseta corretamente os botões a cada pergunta.

class QuizView(ft.View):
    def __init__(self, page, go_to, state=None):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.state = state if state is not None else {}
        self.expand = True

        # Perguntas de exemplo
        self.questions = [
            {
                "q": "Qual era o deus egípcio associado ao submundo e à vida após a morte?",
                "options": ["Rá", "Anúbis", "Hórus", "Ísis"],
                "answer": 1
            },
            {
                "q": "Quem era a deusa mãe e protetora, muitas vezes associada à magia?",
                "options": ["Ísis", "Sekhmet", "Bastet", "Nut"],
                "answer": 0
            },
            {
                "q": "Qual deus era frequentemente representado com cabeça de falcão?",
                "options": ["Osíris", "Hórus", "Anúbis", "Rá"],
                "answer": 1
            }
        ]
        self.index = 0
        self.locked = False

        # fundo e logo
        background = ft.Image(src="background2.png", fit=ft.ImageFit.COVER, expand=True)
        logo = ft.Image(src="anubis_logo.png", width=120, height=120)

        # pergunta
        self.question_text = ft.Text("", size=18, weight=ft.FontWeight.BOLD, selectable=False)

        # botões de alternativas
        self.option_buttons = []
        for i in range(4):
            btn = ft.ElevatedButton(
                text="",
                expand=True,
                height=50,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                on_click=self._make_onclick(i)
            )
            self.option_buttons.append(btn)

        # topo com botão de voltar
        top_row = ft.Row(
            [
                ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS, on_click=lambda _: self.go_to("menu")),
                ft.Container(content=logo, alignment=ft.alignment.center)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        # corpo
        options_column = ft.Column(self.option_buttons, spacing=12)

        content = ft.Column(
            [
                top_row,
                ft.Container(height=20),
                self.question_text,
                ft.Container(height=8),
                options_column
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.controls = [
            ft.Stack([
                ft.Container(content=background, expand=True),
                ft.Container(
                    content=content,
                    expand=True,
                    alignment=ft.alignment.top_center,
                    padding=ft.padding.only(top=30, left=20, right=20)
                )
            ], expand=True)
        ]

        self._load_question()

    def _make_onclick(self, option_index):
        def onclick(e):
            if self.locked:
                return
            self.locked = True
            self._handle_answer(option_index)
        return onclick

    def _reset_buttons(self):
        """Restaura os botões ao estado neutro (sem cores)."""
        for btn in self.option_buttons:
            btn.bgcolor = None
            btn.color = "black"
            btn.disabled = False

    def _load_question(self):
        """Carrega a pergunta atual e reseta visual dos botões."""
        if self.index >= len(self.questions):
            # terminou o quiz
            self.question_text.value = "Você concluiu o quiz! Parabéns!"
            for btn in self.option_buttons:
                btn.text = "-"
                btn.bgcolor = None
                btn.color = "black"
                btn.disabled = True
            self.page.update()
            return

        q = self.questions[self.index]
        self.question_text.value = f"Pergunta {self.index+1}: {q['q']}"

        for i, opt in enumerate(q["options"]):
            btn = self.option_buttons[i]
            btn.text = opt

        self._reset_buttons()
        self.locked = False
        self.page.update()

    def _handle_answer(self, chosen):
        q = self.questions[self.index]
        correct = q["answer"]

        # colore resposta
        if chosen == correct:
            self.option_buttons[chosen].bgcolor = "green"
            self.option_buttons[chosen].color = "white"
            self.state["correct_answers"] = self.state.get("correct_answers", 0) + 1
        else:
            self.option_buttons[chosen].bgcolor = "red"
            self.option_buttons[chosen].color = "white"
            self.option_buttons[correct].bgcolor = "green"
            self.option_buttons[correct].color = "white"

        # atualização de progresso
        self.state["questions_answered"] = self.state.get("questions_answered", 0) + 1
        if self.state.get("questions_answered", 0) >= 1:
            self.state["first_answer"] = True

        # desativa cliques até próxima
        for btn in self.option_buttons:
            btn.disabled = True

        self.page.update()

        # avança automaticamente após 2s
        self.page.run_task(self._delayed_next)

    async def _delayed_next(self):
        await asyncio.sleep(2)
        self.index += 1
        self._load_question()
