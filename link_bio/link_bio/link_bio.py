import reflex as rx
from link_bio.component.navbar import navbar
from link_bio.component.button import button
from link_bio.view.header import header




class State(rx.State):
    pass

def index()-> rx.Component:

    return rx.box(
        
         navbar(),
         rx.vstack(
                header(),
                button("</>FastApi->Login Api","FastApi","braces"),
                button("Web","Web","globe"),
                button("Web","Web","globe"),
                button("Web","Web","globe"),
                button("Web","Web","globe"),
                button("Web","Web","globe"),
                 align= "center",
            ),
            width="100%",
            allign="center",
            height="100%",
            background_color="#262626",
    )
                 



app = rx.App()
    
app.add_page(index)
app._compile()