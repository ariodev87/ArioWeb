import reflex as rx



def card() -> rx.Component:
    return rx.flex(
        rx.card(rx.avatar(src="/pyth.png"),"Python", size="5",),
        rx.card(rx.avatar(src="/fastapi.png"),"FastApi", size="5"),
        rx.card(rx.avatar(src="/reflex.png"),"Reflex", size="5"),
        spacing="2",
    align_items="flex-start",
    flex_wrap="wrap",
    )