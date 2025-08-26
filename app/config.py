# Centralizar toda a nossa configuração

from pydantic_settings import BaseSettings, SettingsConfigDict

# 1. Note como o "modelo de configuração" é estruturado em uma classe.
class Settings(BaseSettings):
    MONGODB_URI: str # 2. Precisamos especificar para o Pydantic que campos estamos procurando.
    DB_NAME: str = "aula2508" #3. Aqui, não só especificamos o tipo, mas o valor exato. Isso é OPCIONAL.
    
    # Configurar o Pydantic para ler o arquivo .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="ignore"
    )

settings = Settings()