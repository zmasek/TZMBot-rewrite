import os
from typing import Tuple

TOKEN: str = os.environ.get("DISCORD_TOKEN", "")
DEV_IDS: Tuple[int] = (int(os.environ.get("DISCORD_DEV_ID", 0)),)
ERROR_CHANNEL_ID: Tuple[int] = (int(os.environ.get("DISCORD_ERROR_CHANNEL", 0)),)
