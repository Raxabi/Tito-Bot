import os
from dotenv import load_dotenv
from src import bot
load_dotenv(".env")

token_var_env = os.environ.get("token")

bot.client.run(token_var_env)