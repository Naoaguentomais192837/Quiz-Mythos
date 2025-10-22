import flet as ft
from view.splash_view import SplashView
from view.start_view import StartView
from view.menu_view import MenuView

# Responsável por inicializar a aplicação, definir tamanho
# da janela e gerenciar a navegação entre as telas.

def main(page: ft.Page):
    page.title = "Mythos"
    page.window_width = 600
    page.window_height = 900
    page.window_resizable = True

# Função para alternar telas 

    def go_to(name):
        page.views.clear()
        if name == "splash":
            page.views.append(SplashView(page, go_to))
        elif name == "start":
            page.views.append(StartView(page, go_to))
        elif name == "menu":
            page.views.append(MenuView(page, go_to))
        page.update()

#Inicia na tela de splash

    go_to("splash")

#Roda o aplicativo

ft.app(target=main, assets_dir="assets")


