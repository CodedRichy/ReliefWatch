import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ReliefWatch"
    debug: bool = False
    
    database_url: str = "postgresql://localhost/reliefwatch"
    
    twitter_api_key: str = ""
    twitter_api_secret: str = ""
    twitter_bearer_token: str = ""
    
    reddit_client_id: str = ""
    reddit_client_secret: str = ""
    
    newsapi_key: str = ""
    
    class Config:
        env_file = ".env"


settings = Settings()
