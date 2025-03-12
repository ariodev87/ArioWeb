import reflex as rx
from link_bio.routes import Route
from link_bio.style.style import Style
from link_bio.pages.index import index
from link_bio.pages.loading_page import login_page




                 

app = rx.App(
         stylesheets=[
        "https://fonts.googleapis.com/css2?family=Doto:wght@100..900&family=Press+Start+2P&display=swap",
        ]
)
app.add_page(index, route=Route.INDEX.value)
app.add_page(login_page, route=Route.API.value)  # Ruta explícita


