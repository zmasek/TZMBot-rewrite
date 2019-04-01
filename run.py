from discord.ext import commands
from datetime import datetime
import config
from config import bot_config
import utils
from os import listdir, chdir
import logging

if __name__ == '__main__':
    chdir(config.project_dir)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
handler.setLevel(logging.WARNING)
logger.addHandler(handler)

handler = logging.FileHandler(filename='debug.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix="!")
client.config = bot_config
client.utils = utils

@client.event
async def on_ready():
    print(f"Bot running on {client.user} (ID: {client.user.id})")
    print(f"Took {datetime.now()-launch_time}, Time now {datetime.now()}")

if __name__ == '__main__':
    for filename in listdir(config.relative_cogs_dir):
        if filename.endswith('.py'):
            try:
                client.load_extension(f"{config.relative_cogs_dir}.{filename[:-3]}")
                print(f"-\tCog extension {filename} loaded successfully")
            except Exception as e:
                print(f"-\tCog extension {filename} could not be loaded: {e}")

    launch_time = datetime.now()
    print(f"Attempting to run bot at {launch_time}\n---------------------------------------------------------------------")
    client.run(config.token)
