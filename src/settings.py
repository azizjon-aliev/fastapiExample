from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    
    # database 
    db_connection: str
    db_name: Optional[str] = None
    db_user: Optional[str] = None
    db_password: Optional[str] = None
    db_host: Optional[str] = None
    db_port: Optional[int] = None
    db_url: Optional[str] = None
    
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        if self.db_url is None:
            self.db_url = f"{self.db_connection}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    
    
    

settings = Settings()