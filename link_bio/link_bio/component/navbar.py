import reflex as rx
from link_bio.style.style import Style



def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.link(
            rx.text(
                "<../ArioDev>",
                font_family="Doto",
                font_size=30,
                #color_scheme='blue',
                
                
                size='5',
                high_contrast=True,                
                style={"margin_left": "60px","margin_top": "25px","color":"white",}, # Usa CSS para margen personalizado
            ),
            href="/"
            ),
            position="fixed",
            top="0",
           bg=Style.SECUNDARY_COLOR,
           width="100%",
           height="5em",
           style={"box-shadow": "0px 0px 10px rgba(1, 1, 1, 1)"}
        ),
        
    )
                





    
    