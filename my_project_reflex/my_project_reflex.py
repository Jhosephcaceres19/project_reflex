"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

def my_button2():
    return rx.button("hacer click"),

def my_div():
    return rx.el.div(
        rx.el.p("Hola soy Jhoseph desarrollador frontend con un amplio aprendisaje continuo")
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Hola Jhoseph", size="9"),
            rx.text(
                "este es tu pagina principal",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            rx.button("INGRESAR"),
            rx.box(
                rx.text("esto es un boton"),
                rx.button("HACER CLICK", border_radius="15px", font_size="18px"),
                my_button2(),
            ),
            my_div(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
