import reflex as rx
from link_bio.style.style import Style



def headerText(HeaderText:str) -> rx.Component:
    return rx.text(HeaderText,size="8",color=Style.HEADER_COLOR.value)