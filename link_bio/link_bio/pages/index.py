import reflex as rx
from link_bio.component.footer import footer_item
from link_bio.component.card import card
from link_bio.component.navbar import navbar
from link_bio.component.button import button
from link_bio.view.header import header
from link_bio.view.headertext import headerText
from link_bio.style.style import Style
from link_bio.routes import  Route
from link_bio.state.page_state import IndexState


      
      


@rx.page(
        #IndexState.GetTemperatura
       route=Route.INDEX.value,
       on_load=IndexState.GetInitialData
)
def index()-> rx.Component:

    return rx.box(
        
         navbar(IndexState.icono,IndexState.temperatura),
          
         rx.vstack(
               
                header(),
                
                headerText("Proyectos"),
                
                button("</>FastApi->Login Api","FastApi","braces",Style.BUTTON_BORDER_GREEN,Route.API.value,False),
                button("</IA>","@@Aplicación integrada con ChatGPT ","globe",Style.BUTTON_BORDER_RED,"https://github.com/ariodev87/",True),
                button("Librería", "Aplicación que gestiona una librería","globe",Style.NO_BUTTON_BORDER,"https://pivigames.blog/",True),
                button("Web","Web","globe",Style.NO_BUTTON_BORDER,"https://userapi-9s41.onrender.com/",True),
                headerText("Tecnologías"),
                card(),
                
                 align= "center",
            ),
            footer_item(),
            
            width="100%",
            min_height="100vh",  # Altura mínima igual al viewport
            overflow_y="auto",
            background_color=Style.PRIMARI_COLOR,
            
          
    )