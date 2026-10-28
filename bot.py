from dotenv import load_dotenv
import discord
import requests
import os
from discord import app_commands
from handler import register_handlers
from commands import register_commands
from reminders import start_reminders
import database.postgres as db
import database.mongodb as mongo

load_dotenv()

JOKES_URL = "https://raw.githubusercontent.com/EspresSoHin/Discord-Bot/refs/heads/Develop/crowkittenjokes.json"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class Mephisto(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) #do what you gotta do as a discord Client, then add the command tree
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await db.init_pool()
        await mongo.init_mongo()
        self.jokelist = requests.get(JOKES_URL).json()
        register_commands(self.tree)
        await self.tree.sync()

client = Mephisto(intents=intents)


##########################
#   Bot Initialization   #
########################## 


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    for guild in client.guilds:
        await db.add_server(guild.id, guild.name)

    test_channel_id = os.environ.get("TEST_CHANNEL_ID")
    if test_channel_id:
        await client.get_channel(int(test_channel_id)).send("Mephisto has awoken.")
    
    start_reminders(client)


register_handlers(client)
client.run(os.environ["TOKEN"])