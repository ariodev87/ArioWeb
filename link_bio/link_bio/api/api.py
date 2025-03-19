import requests


from link_bio.style.enlace import link

async def SayHello()->str:
    return  link.API_USER_LOGIN.value

#API clima

async def GetClima():
    response= requests.get("https://www.el-tiempo.net/api/json/v2/provincias/28/municipios/28079")
    if response.status_code==200:
        return response.json()
    return "Error"
