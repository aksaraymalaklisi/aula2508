# Centralizar toda a nossa configuração

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MONGODB_URI: str
    DB_NAME: str = "aula2508"
    
    # Configurar o Pydantic para ler o arquivo .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="ignore"
    )

settings = Settings()