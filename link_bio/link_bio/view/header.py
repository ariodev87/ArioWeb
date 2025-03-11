import reflex as rx



def header() -> rx.Component:
    return rx.box( 
rx.vstack(        
         rx.hstack(             
             
            rx.avatar(fallback="AR", radius="full",color="#999999",size="6",style={"margin": "0px",},aling="center",
                      src="/ario.jpg",
                      ),
            rx.vstack(
            rx.text("Ariel Castro García",color="#999999",size="3",padding_top="20px"),
            rx.flex(
                rx.link(
                rx.icon("github",color="#999999"),
                href="https://github.com/ariodev87",
                ),
                rx.link(
                rx.icon(tag="linkedin",color="#999999"),
                href="https://www.linkedin.com/in/arielcastro-insanestudios/",
                ),
               gap="10px",
                #padding_top="100px",
            ),
                ),
                 padding_right="10em",
           
         ),
         rx.text("Ingeniero Informático graduado de la Universidad de Ciencias Informáticas (UCI),"
                 " con experiencia en desarrollo de software utilizando lenguajes como C# y PHP."
                 " Especializado en administración de redes y seguridad informática, he ampliado"
                 " mis habilidades en programación con Python, trabajando con frameworks como FastAPI"
                 " y Reflex para crear aplicaciones web escalables e interactivas.",
                 padding_top="20px",color="#999999",padding_right="10em",font_family="Press Start 2P",font_size="clamp(14px, 1.5vw, 10px)",),
            
        width="50em",
        padding_top="10em",
        margin_left="10em",
        align="center",
        
        height="100%",
        
    )
      
    )