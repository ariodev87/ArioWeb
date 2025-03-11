import reflex as rx
from link_bio.component.footer import footer_item
from link_bio.component.card import card
from link_bio.component.navbar import navbar
from link_bio.component.button import button
from link_bio.view.header import header
from link_bio.view.headertext import headerText
from link_bio.style.style import Style
from link_bio.routes import Route


@rx.page(
        route=Route.API.value,
)
def login_page()-> rx.Component:

    return rx.box(
        
         navbar(),
          
         rx.vstack(
                header(),
                
                headerText("Proyectos"),
                button("</>FastApi->Login Api","FastApi","braces",Style.BUTTON_BORDER_GREEN,"https://userapi-9s41.onrender.com/",True),
               
                card(),
                
                 align= "center",
            ),
            footer_item(),
            
            width="100%",
            min_height="100vh",  # Altura mínima igual al viewport
            overflow_y="auto",
            background_color=Style.PRIMARI_COLOR.value,
            
          
    )