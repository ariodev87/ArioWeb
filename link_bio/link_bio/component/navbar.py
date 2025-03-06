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
           bg="#1a1a1a",
           width="100%",
           style={"box-shadow": "0px 0px 10px rgba(0, 0, 0, 0.5)"}
        ),
        
    )
                





    
    