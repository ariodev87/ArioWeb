import reflex as rx
from link_bio.api.api import SayHello,GetClima,getuser_api

class IndexState(rx.State):
    hellomsg: str = ""  # Inicializa la variable de estado con un string vacío
    temperatura:str=""
    clima:str=""
    icono:str=""
    login:str=""
    userlist:list
    primerusuario:str=""

    async def callhello(self):
        self.hellomsg = await SayHello()  # Asigna el valor al atributo del estado

    async def GetTemperatura(self):
        datos_temperatura = await GetClima()
        self.temperatura= datos_temperatura["temperatura_actual"]


    async def GetaClima(self):
        datos_clima = await GetClima()
        statesky= datos_clima["stateSky"]
        self.clima=statesky["description"]
        if self.clima=="Cubierto" or self.clima=="Nuboso" or self.clima=="Poco nuboso" or self.clima=="Muy nuboso" :
            self.icono="/nublado(2).png"
        else:
            if self.clima=="Despejado":
                self.icono="/soleado.png"
            else:
                if self.clima=="Cubierto con lluvia escasa" or self.clima=="Cubierto con tormenta y lluvia escasa" or self.clima=="Nubes altas":
                    self.icono="/lluvia.png"
   
    async def getuserdata(self):
        self.userlist= await getuser_api()
        if self.userlist is not None and len(self.userlist)>0:
            for item in self.userlist:
                self.primerusuario=str(item["user"])
        else:                
         self.primerusuario="Lista Vacia"
         self.userlist = []          
    
        


    
 
        
        
    async def GetInitialData(self):
        await self.GetaClima()
        await self.GetTemperatura()
        await self.getuserdata()


