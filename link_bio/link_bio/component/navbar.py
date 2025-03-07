import reflex as rx



def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            
            rx.text(
                "Ario",
                #color_scheme='blue',
                size='5',
                high_contrast=True,                
                style={"margin": "10px","color":"white",}, # Usa CSS para margen personalizado
            ),
            position="fixed",
            top="0",
           bg="#0c1727",
           width="100%",
           height="5em",
           #style={"box-shadow": "0px 0px 10px rgba(1, 1, 1, 1)"}
        ),
        
    )
                





    
    