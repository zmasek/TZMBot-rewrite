import os

import discord
from config import PROJECT_DIR, RELATIVE_COGS_DIR


async def strikethrough(message: discord.Message, new_message: str = ""):
    await message.edit(content=f"~~{message.content}~~ {new_message}")
    try:
        await message.clear_reactions()
    except discord.Forbidden:
        pass


def get_cogs():
    return [
        f"{RELATIVE_COGS_DIR}.{filename[:-3]}"
        for filename in os.listdir(os.path.join(PROJECT_DIR, RELATIVE_COGS_DIR))
        if filename.endswith(".py") and "__init__" not in filename
    ]
