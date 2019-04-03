import datetime
import logging

from config import TOKEN
from discord.ext import commands
from utils import get_cogs

logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
stream_handler.setLevel(logging.WARNING)
logger.addHandler(stream_handler)

file_handler = logging.FileHandler(filename="debug.log", encoding="utf-8", mode="a")
file_handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(file_handler)

client = commands.Bot(command_prefix="?")


@client.event
async def on_ready():
    logger.info(f"Bot running on {client.user} (ID: {client.user.id})")
    logger.info(
        f"Took {datetime.datetime.now()-launch_time}, Time now {datetime.datetime.now()}"
    )


if __name__ == "__main__":
    for cog in get_cogs():
        try:
            client.load_extension(cog)
            logger.info(f"-\tCog extension {cog} loaded successfully")
        except Exception as e:
            logger.info(f"-\tCog extension {cog} could not be loaded: {e}")

    launch_time = datetime.datetime.now()
    logger.info(f"Attempting to run bot at {launch_time}")
    client.run(TOKEN)
