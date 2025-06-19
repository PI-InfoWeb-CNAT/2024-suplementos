import os

TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres:Lb160785@localhost:5432/powerup_db"
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}