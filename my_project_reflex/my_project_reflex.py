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
    ),

def contentRigth():
    return rx.box(
        rx.el.div(
            rx.link(
                rx.icon("github"),
                href="https://jhosephcaceres.vercel.app/",
                gap="2",
            ),
            rx.link(
                rx.icon("facebook")
            ),
            rx.link(
                rx.icon("instagram")
            ),
            rx.link(
                rx.icon("linkedin")
            ),
            rx.link(
                rx.icon("twitch")
            ),
            rx.link(
                rx.icon("twitter")
            ), class_name="flex flex-row gap-4"
        ), class_name="flex flex-row"
    ),

def image():
    return rx.image(
        src="https://images.squarespace-cdn.com/content/v1/6534a4725af2f11191967432/bd3a2456-d1d7-4b25-a7bb-b8b3ab7070b9/software-development-user-experience.png",
        width="700px",
        height="auto",
        border_radius="50px"
    )



def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        header(),
        rx.color_mode.button(position="top-right"),
        rx.vstack(
           rx.el.div(
    # Columna izquierda
                rx.el.div(
                rx.heading("Hi There,", size="9", class_name="text-4xl font-bold"),
                rx.heading("I'm Jhoseph Caceres", class_name="text-3xl font-semibold"),
                rx.text("I Am Into Web Develop!", class_name="text-lg text-blue-500"),
                rx.link(
                    rx.button("About Me", class_name="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"),
                    href="https://jhosephcaceres.vercel.app/",
                    is_external=True,
                ),
                contentRigth(),
                class_name="flex flex-col gap-4 max-w-lg"
            ),

    # Columna derecha (imagen)
            rx.hstack(
                image(),
                class_name="flex justify-center items-center"
            ),

    # Contenedor principal
                class_name=(
                    "w-full h-[700px] flex flex-row items-center justify-around px-10 "
                ),
            ),

            spacing="5",
            # justify="start",
            min_height="100px",
        ),
    )


app = rx.App()
app.add_page(index)
