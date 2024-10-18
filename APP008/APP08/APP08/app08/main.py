import flet as ft


def main(page: ft.Page):
    
    page.window_width=800
    page.window_height=800
    
    page.bgcolor="black"
    page.title="mictlan"
    page.fgcolor="gray"
    
    intro=ft.Audio(src="intro.mp3",volume=1,balance=0)
    page.overlay.append(intro)
    nivel1=ft.Audio(src="primer_Nivel:mp3")
