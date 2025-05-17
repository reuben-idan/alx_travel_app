import environ
import os

env = environ.Env(
    DEBUG=(bool, False)
)

# reading .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
