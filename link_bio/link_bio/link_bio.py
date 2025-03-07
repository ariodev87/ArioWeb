import reflex as rx
from link_bio.component.footer import footer_item
from link_bio.component.navbar import navbar
from link_bio.component.button import button
from link_bio.view.header import header
from link_bio.view.headertext import headerText
from link_bio.style.style import Style



class State(rx.State):
    pass

def index()-> rx.Component:

    return rx.box(
        
         navbar(),
          
         rx.vstack(
                header(),
                headerText("Proyectos"),
                button("</>FastApi->Login Api","FastApi","braces",Style.BUTTON_BORDER_GREEN),
                button("Web","Web","globe",Style.BUTTON_BORDER_RED),
                button("Web","Web","globe",Style.NO_BUTTON_BORDER),
                button("Web","Web","globe",Style.NO_BUTTON_BORDER),
                spacing="3",
                 align= "center",
            ),
             footer_item(),
            width="100%",
            allign="center",
            height="50em",
            background_color=Style.PRIMARI_COLOR,
          
    )
                 



app = rx.App()
    
app.add_page(index)
app._compile()