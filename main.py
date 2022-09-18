from os import environ
from dotenv import load_dotenv
from src.bot import client

load_dotenv(".env")
token_var_env = environ.get("token")

client.run(token = token_var_env)