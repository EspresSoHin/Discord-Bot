import os
from dotenv import load_dotenv
from pymongo import AsyncMongoClient
from urllib.parse import quote_plus
from datetime import datetime, timezone


load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = quote_plus(os.getenv("MONGO_PASSWORD")) #keep encoded if you modify the password later
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_DB = os.getenv("MONGO_DB", "MephistoBot")

MONGO_URI = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/?appName=MephistoBot"

client = AsyncMongoClient(MONGO_URI, tz_aware=True, serverSelectionTimeoutMS=5000)
mongo_db = client[MONGO_DB]

async def init_mongo():
    await client.admin.command("ping")
    await mongo_db["stats"].create_index("guild_id", unique=True)


##########################################################################################################################
# ------------------------------------------ Incrementation of stats ----------------------------------------------------#
##########################################################################################################################


async def increment_stat(guild_id: int, counter: str, amount: int = 1):
    await mongo_db["stats"].update_one(
        {"guild_id": guild_id},
        {"$inc": {f"counters.{counter}": amount}, #$inc adds amount to counter 
         "$set": {"updated_at": datetime.now(timezone.utc)}},
        upsert=True)

async def get_stats(guild_id: int) -> dict:
    doc = await mongo_db["stats"].find_one({"guild_id": guild_id})
    return doc["counters"] if doc else {}

async def delete_stats(guild_id: int):
    await mongo_db["stats"].delete_one({"guild_id": guild_id})