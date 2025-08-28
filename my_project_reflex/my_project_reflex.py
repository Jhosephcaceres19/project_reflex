"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""


class CounterState(rx.State):
    count: int =0

    @rx.event
    def increment(self):
        self.count += 1

    @rx.event
    def decrement(self):
        self.count -= 1

    @rx.event
    def increment_encinco(self, amount: int):
        self.count += amount

    @rx.event
    def decrementar_encinco(self, amount: int):
        self.count -= amount

def counter_increment():
    return rx.hstack(
        rx.heading(CounterState.count),
        rx.button(
            "Incrementar", on_click=CounterState.increment
        ),
        rx.button(
            "Decrementar", on_click=CounterState.decrement
        ),
        rx.button(
            "Incrementar en 5", on_click=CounterState.increment_encinco(5)
        ),
        rx.button(
            "Decrementar en 5", on_click=CounterState.decrementar_encinco(5)
        )
    ),


def my_button2():
    return rx.button("hacer click"),

def my_div():
    return rx.el.div(
        rx.el.p("Hola soy Jhoseph desarrollador frontend con un amplio aprendisaje continuo")
    ),

def roun_button():
    return rx.button(
        "Hacer click", border_radius="15px", font_size="18px"
    ),

def header():
    return rx.box(
        rx.el.div(
            # Título
            rx.el.div(
                "YOUR WEBSITE",
                class_name="text-2xl font-bold "
            ),
            # Botones de navegación
            rx.hstack(
                rx.button("Home", class_name="px-4 py-2 rounded-lg hover:bg-blue-200"),
                rx.button("About us", class_name="px-4 py-2 rounded-lg hover:bg-blue-200"),
                rx.button("Work", class_name="px-4 py-2 rounded-lg hover:bg-blue-200"),
                rx.button("Info", class_name="px-4 py-2 rounded-lg hover:bg-blue-200"),
                rx.button("Get Started", class_name="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-100"),
                class_name="flex gap-4 items-center justify-end w-1/2 m-t-8"
            ),
            class_name="flex flex-row justify-between items-center w-full"
        ),
        class_name="p-6 w-full shadow-md"
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        header(),
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
            roun_button(),
            counter_increment(),

            rx.box(
                "holaa como estas",
                class_name="text-4xl text-center text-red-200"
            ),



            spacing="5",
            # justify="start",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
