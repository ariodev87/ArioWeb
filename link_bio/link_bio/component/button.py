import reflex as rx
from link_bio.style.style import Style


def button(text1:str,text2:str,iconTag:str,borderColor:str,) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.icon(iconTag, size=16,margin_top="1em"),
            rx.vstack(
                rx.text(text1, size="2"),
              
              rx.text(text2, size="1"),

            ),
          #align="center",  # Alinea verticalmente al centro
            
        ),
        
        style={"_hover": {"background": "#00004d"},"border": borderColor},
        background_color=Style.BUTTON_COLOR.value,
        width="25%",
        height="5em",
        radius="large",
        display="block",
        padding_lef="10em",
       
        #style={"font-size": "12px"}  # Reduce el tamaño de la fuente
    )