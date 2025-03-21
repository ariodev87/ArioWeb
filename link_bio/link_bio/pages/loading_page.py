import reflex as rx
from link_bio.component.footer import footer_item
from link_bio.component.card import card
from link_bio.component.navbar import navbar
from link_bio.component.button import button
from link_bio.view.header import header
from link_bio.view.headertext import headerText
from link_bio.style.style import Style
from link_bio.routes import Route
from link_bio.state.page_state import IndexState


@rx.page(
        route=Route.API.value,
       
       on_load=IndexState.GetInitialData
)

def login_page()-> rx.Component:

    return rx.box( 
        navbar(IndexState.icono,IndexState.temperatura),
        rx.center( 
        rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/Designer(22).png",
                    width="5em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading(
                    "Sign in to your account",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Email address",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="user@reflex.dev",
                    type="email",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                    ),
                    rx.link(
                        "Forgot password?",
                        href="#",
                        size="3",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    placeholder="Enter your password",
                    type="password",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Sign in", size="3", width="100%"),
            rx.center(
                rx.text("New here?", size="3"),
                rx.link("Sign up", href="#", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="28em",
        width="100%",
        margin_top=200,
        align="center"
    ),),)