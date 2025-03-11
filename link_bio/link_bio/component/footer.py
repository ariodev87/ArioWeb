import reflex as rx
from link_bio.style.style import Style

def footer_item() -> rx.Component:
    return  rx.box(    
        rx.flex(        
            rx.heading(
                 "<../ArioDev>",
                font_family="Doto",
                #color_scheme='blue',
                size='5',
                high_contrast=True,                
                                
            ),
            rx.text("Creado por Ariel Castro , Tecnologia Reflex"),
            direction="column",  # Apila los elementos verticalmente
            align_items="center",  # Centra los elementos horizontalmente
            justify_content="center",
            padding_bottom=20,

                 ),
                
           bg=Style.SECUNDARY_COLOR,
           width="100%",
           height="100%",
           style={"box-shadow": "0px 0px 10px rgba(1, 1, 1, 1)"},
          
            padding_top=30,
           z_index="1000",
           margin_top="2em",
           bottom="0",
           align="center",
           ),
        