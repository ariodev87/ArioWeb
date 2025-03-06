import reflex as rx



def header() -> rx.Component:
    return rx.box( 
rx.vstack(        
         rx.hstack(             
             
            rx.avatar(fallback="AR", radius="full",color="#999999",size="6",style={"margin": "0px",},aling="center"),
            rx.vstack(
            rx.text("Ariel Castro García",color="#999999",size="3",padding_top="20px"),
            rx.flex(
                rx.icon("github",color="#999999"),
                rx.icon(tag="linkedin",color="#999999"),
               gap="10px",
                #padding_top="100px",
            ),
                ),
                 padding_right="10em",
           
         ),
         rx.text("Un texto narrativo es aquel que ofrece al lector una narración"
                 ", con sus personajes, escenarios y acontecimientos. Estos relatos "
                 "pueden ser reales o imaginarios y pueden formar parte de la historia,"
                 " la literatura o la narración popular. Por ejemplo: los cuentos, las leyendas, las novelas o las crónicas de viaje",
                 padding_top="20px",size="2",color="#999999",padding_right="10em",),
            
        width="40em",
        padding_top="50px",
        margin_left="10em",
        align="center",
        height="100%",
        
    )
      
    )