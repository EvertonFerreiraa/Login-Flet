import flet as ft
from flet import (AlertDialog, Column, Container, MainAxisAlignment, Page, Row,
                  ScrollMode, Text, TextButton, TextField, TextThemeStyle,
                  ThemeMode, UserControl)


class LoginPage(UserControl):
    def __init__(self):
        super().__init__()
        self.text_ini = Text(
            value="Digite Usuário e Senha:",
            style=TextThemeStyle.TITLE_MEDIUM,
            color=ft.colors.WHITE,
        )
        self.textfild_user = TextField(
            label="Usuário",
            icon=ft.icons.PERSON,
        )
        self.textfild_password = TextField(
            label="Senha",
            icon=ft.icons.PASSWORD,
            password=True,
        )
        self.button_login = TextButton(
            text="Entrar",
        )
        self.button_exit = TextButton(
            text="Sair",
        )
        self.button_register = TextButton(
            text="Registrar"
        )

    def build(self):
        return Container(
            alignment=ft.alignment.center,
            margin=ft.margin.all(100),
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.text_ini,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.textfild_user,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.textfild_password,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.button_login,
                            self.button_exit,
                            self.button_register,
                        ]
                    ),
                ]
            )
        )


class RegisterPage(UserControl):
    def __init__(self):
        super().__init__()
        self.text_ini = Text(
            value="Para se registrar preencha o formulário:",
            style=TextThemeStyle.TITLE_MEDIUM,
            color=ft.colors.WHITE,
        )
        self.textfield_name = TextField(
            label="Nome de Usuário",
            icon=ft.icons.PERSON,
        )
        self.textfield_password = TextField(
            label="Senha de Acesso",
            icon=ft.icons.PASSWORD,
            password=True,
        )
        self.textfield_password_confirm = TextField(
            label="Confirme a Senha",
            icon=ft.icons.PASSWORD,
            password=True,
        )
        self.button_register = TextButton(
            text="Confirmar",
        )
        self.button_back = TextButton(
            text="Voltar",
        )

    def build(self):
        return Container(
            alignment=ft.alignment.center,
            margin=ft.margin.all(100),
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.text_ini,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.textfield_name,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.textfield_password,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.textfield_password_confirm,
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.button_register,
                            self.button_back,
                        ]
                    )
                ]
            )
        )


def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.title = "Sistema de Login Simples"
    page.scroll = ScrollMode.ALWAYS

    def clicked_reg_db(e):

        user = register_page.textfield_name.value
        password = register_page.textfield_password.value
        password_conf = register_page.textfield_password_confirm.value

        if user != '' and password == password_conf:
            page.clean()
            page.add(
                Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(250),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value=f"Bem Vindo, {user} ",
                                style=TextThemeStyle.TITLE_LARGE,
                                color=ft.colors.GREEN
                            )
                        ]
                    )
                )
            )
            page.update()

        if user == '':
            page.clean()
            page.add(
                Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(10),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value="Digite Seu Nome de Usuário!",
                                style=TextThemeStyle.TITLE_LARGE,
                                color=ft.colors.RED
                            )
                        ]
                    )
                )
            )
            page.update()
            page.add(
                register_page
            )

        if user and password == '' or password_conf == '':
            page.clean()
            page.add(
                Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(10),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value="Preencha os campos de senha!",
                                style=TextThemeStyle.TITLE_LARGE,
                                color=ft.colors.RED
                            )
                        ]
                    )
                )
            )
            page.update()
            page.add(
                register_page
            )

        if password != password_conf:
            page.clean()
            page.add(
                Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(10),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value="As senhas não conferem!",
                                style=TextThemeStyle.TITLE_LARGE,
                                color=ft.colors.RED
                            )
                        ]
                    )
                )
            )
            page.update()
            page.add(
                register_page
            )

    def clicked_reg_back(e):
        page.clean()
        page.add(
            login_page
        )

    register_page = RegisterPage()
    register_page.button_register.on_click = clicked_reg_db
    register_page.button_back.on_click = clicked_reg_back

    def clicked_login(e):
        pass

    def clicked_exit(e):
        def exit_confirm(e):
            page.window_close()

        def close_dialog(e):
            dialog.open = False
            page.update()

        dialog = AlertDialog(
            modal=True,
            title=Text("Por Favor, Confirme:"),
            content=Text("Você tem certeza que deseja sair?"),
            actions=[
                TextButton(
                    text="Sim",
                    on_click=exit_confirm
                ),
                TextButton(
                    text="Não",
                    on_click=close_dialog
                ),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

        page.dialog = dialog
        dialog.open = True
        page.update()

    def clicked_register(e):
        page.clean()
        page.add(
            register_page,
        )

    login_page = LoginPage()
    login_page.button_login.on_click = clicked_login
    login_page.button_exit.on_click = clicked_exit
    login_page.button_register.on_click = clicked_register

    page.add(
        login_page,
    )


ft.app(target=main)
