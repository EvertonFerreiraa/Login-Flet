import flet as ft
from flet import TextButton, TextThemeStyle, Text, MainAxisAlignment, ScrollMode, Page, TextField, Container, Column, Row
import database


def main(page: Page):
    
    page.scroll = ScrollMode.ALWAYS


    def clicked_enter(e):
        pass
    
    def clicked_exit(e):
        pass

    def clicked_register(e):
        page.clean()
        page.add(
            Container(
                Column(
                    controls=[
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                Text(
                                    value="Formulário de Registro",
                                    color=ft.colors.BLACK,
                                    style=TextThemeStyle.TITLE_MEDIUM
                                )
                            ]
                        ),
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                TextField(
                                    label="Nome Completo",
                                    icon=ft.icons.PERSON,
                                ),
                            ]
                        ),
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                TextField(
                                    label="Digite uma Senha",
                                    password=True,
                                    icon=ft.icons.PASSWORD
                                )
                            ]
                        ),
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                TextField(
                                    label="Confirme a Senha",
                                    password=True,
                                    icon=ft.icons.PASSWORD
                                )
                            ]
                        ),
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                TextButton(
                                    text="Confirmar",
                                )
                            ]
                        ),
                    ]
                )
            )
        )

    # Adicionar os Controles
    page.add(
        Container(
        alignment=ft.alignment.center,
            content=Column(
                        controls=[
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Text(
                                        value="Digite Usuário e Senha",
                                        style=TextThemeStyle.TITLE_MEDIUM,
                                        color=ft.colors.BLACK,
                                    ),
                                ]
                            ),
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    TextField(
                                        label="Usuário",
                                        icon=ft.icons.PERSON
                                    ),
                                ]
                            ),
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    TextField(
                                        label="Senha",
                                        icon=ft.icons.PASSWORD
                                    ),
                                ]
                            ),
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    TextButton(
                                        text="Entrar",
                                        on_click=clicked_enter,
                                    ),
                                    TextButton(
                                        text="Sair",
                                        on_click=clicked_exit
                                    ),
                                    TextButton(
                                        text="Registrar",
                                        on_click=clicked_register
                                    ),
                                ]
                            ),
                        ]
                        )
                        )
                    )

    page.update()

ft.app(target=main)
