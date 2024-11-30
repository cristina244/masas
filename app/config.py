# config.py
class Settings:
    SECRET_KEY = "mysecretkey"  # Cambia esto por una clave más segura
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()
