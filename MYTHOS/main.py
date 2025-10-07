import flet as ft
from view.splash_view import SplashView
from view.start_view import StartView
from view.menu_view import MenuView

def main(page: ft.Page):
    page.title = "Mythos"
    page.window_width = 600
    page.window_height = 900
    page.window_resizable = True

    def go_to(name):
        page.views.clear()
        if name == "splash":
            page.views.append(SplashView(page, go_to))
        elif name == "start":
            page.views.append(StartView(page, go_to))
        elif name == "menu":
            page.views.append(MenuView(page, go_to))
        page.update()

    go_to("splash")

ft.app(target=main, assets_dir="assets")



