import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    DATABASE_URI = 'sqlite:///database/search_engine.db'
    for key, value in os.environ.items():
        print(f'{key}: {value}') 