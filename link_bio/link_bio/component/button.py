import reflex as rx

def button(text1:str,text2:str,iconTag:str) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.icon(iconTag, size=16,margin_top="1em"),
            rx.vstack(
                rx.text(text1, size="2"),
              
              rx.text(text2, size="1"),

            ),
          #align="center",  # Alinea verticalmente al centro
            
        ),
        background_color="#1a1a1a",
        hover={"background_color": "#262626"},
        width="25%",
        height="5em",
        radius="large",
        display="block",
        padding_lef="10em",
        state_hovered="#262626",
        #style={"font-size": "12px"}  # Reduce el tamaño de la fuente
    )