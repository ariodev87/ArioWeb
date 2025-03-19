import reflex as rx
from link_bio.style.style import Style



def navbar(imagen:str="/soleado.png",temperatura:str=0) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.hstack(
            rx.link(
            rx.text(
                "<../ArioDev>",
                font_family="Doto",
                font_size=30,
                size='5',
                high_contrast=True,                
                style={"margin_left": "60px","margin_top": "25px","color":"white",}, # Usa CSS para margen personalizado
            ),
            href="/"
            ),
            rx.image(src={imagen}, width="2em",
                     margin_top=25,
                     margin_left="50em",
                     ),
            rx.text(temperatura,margin_top=30,),         
            
           
            position="fixed",
            top="0",
           bg=Style.SECUNDARY_COLOR,
           width="100%",
           height="5em",
           style={"box-shadow": "0px 0px 10px rgba(1, 1, 1, 1)"}
        ),
        ),
         
        
    )
                





    
    