import os

from starlette.config import Config


dir_path = os.path.dirname(os.path.realpath(__file__))
root_dir = dir_path[:-3]
config = Config(f'{root_dir}.env')

DB_USER = config('DB_USER', cast=str)
PASSWORD = config('PASSWORD', cast=str)
DB_HOST = config('DB_HOST', cast=str)
DB_PORT = config('DB_PORT', cast=str)
DB_NAME = config('DB_NAME', cast=str)
APP_HOST = config('APP_HOST', cast=str)
APP_PORT = config('APP_PORT', cast=str)

DB_URL = f'postgresql://{DB_USER}:{PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'