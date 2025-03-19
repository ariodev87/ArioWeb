import reflex as rx

config = rx.Config(
    app_name="link_bio",
    cors_allowed_origins=[
        "http://localhost:8000",
        "http://localhost:8002",
        "http://localhost:3000",
        "http://localhost:3002",
        "http://localhost:*",
        "https://arioweb-2.onrender.com",
        "https://ariodev.vercel.app/",
        "https://ario-web-pied.vercel.app/",
        
                ]
        )

