import reflex as rx

config = rx.Config(
    app_name="link_bio",
    cors_allowed_origins=[
        "http://localhost:8000",
        "http://localhost:3000",
        "https://arioweb-2.onrender.com",
                ]
        )

