import os
from supabase import create_client, Client
from dotenv import load_dotenv

class SupabaseAPI:

    url: str =("https://fqlgirxqhwpytyihaoyi.supabase.co")
    key: str =("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZxbGdpcnhxaHdweXR5aWhhb3lpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDI1NTA1ODIsImV4cCI6MjA1ODEyNjU4Mn0.U5Ih-wGUnfIkraNOfpBzDQLTEgeLuBwqzkfraG3PUa0")
    supabase: Client = create_client(url, key)

    def getuser(self)->list:
        response = self.supabase.table("users").select("*").execute()
        user_data=[]

        if len(response.data)>0:
            for user_item in response.data:
                user_data.append(user_item)
            
            return user_data