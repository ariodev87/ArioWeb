import reflex as rx

def footer_item() -> rx.Component:
    return  rx.box(    
        rx.flex(        
            rx.heading(
                "pepe",
                #color_scheme='blue',
                size='5',
                high_contrast=True,                
                style={"margin": "30px","color":"white",}, # Usa CSS para margen personalizado
            ),
            rx.box(
            rx.vstack(
                rx.text("aaaaaaaaaaaaaaaaaaaa"),
                 rx.text("aaaaaaaaaaaaaaaaaaaa"),
                 ),
                 width="60em",
                 ),
                
           bg="#000d33",
           width="100%",
           heigth="60em",
           style={"box-shadow": "0px 0px 10px rgba(1, 1, 1, 1)"},
           # margin_left="2em",
           ),
        ),