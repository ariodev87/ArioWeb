import os
from supabase import create_client, Client
from dotenv import load_dotenv

class SupabaseAPI:
    def __init__(self):
        load_dotenv()  # Carga las variables de entorno desde .env
        self.url = os.getenv("SUPABASE_URL")  # Carga la URL desde la variable de entorno o usa el valor por defecto
        self.key = os.getenv("SUPABASE_KEY")  # Carga la clave desde la variable de entorno o usa el valor por defecto
        self.supabase = create_client(self.url, self.key)

    def getuser(self)->list:
        response = self.supabase.table("users").select("*").execute()
        user_data=[]

        if len(response.data)>0:
            for user_item in response.data:
                user_data.append(user_item)
            
            return user_data
        print( "Error de conexion")
