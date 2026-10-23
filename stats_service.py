import random
from pymongo.errors import PyMongoError
import database.mongodb as mongo

COUNTERS = ["caw", "pats", "gems", "bubblewrap", "jokes", "stalkers"]


async def record(guild_id: int, counter: str, amount: int = 1):
    if counter not in COUNTERS:
        raise ValueError(f"Unknown counter: {counter}")
    try:
        await mongo.increment_stat(guild_id, counter, amount)
    except PyMongoError as e: #If Mongo breaks, bot still works
        print(f"Stat not recorded ({counter}): {e}")


async def mephisto_report(guild_id: int) -> str:
    killed = random.randint(1, 10)                # hehehehe
    await record(guild_id, "stalkers", killed)

    s = await mongo.get_stats(guild_id)
    return (
        "*Sylus voice in Mephisto's speakers:* Status report, kitten.\n\n"
        f"𓅨 Caws cawed: {s.get('caw', 0)}\n"
        f"☄ Pats received: {s.get('pats', 0)}\n"
        f"⌔⌔ Gems collected: {s.get('gems', 0)}\n"
        f"｡˚○ Bubble wraps summoned: {s.get('bubblewrap', 0)}\n"
        f"♡ Jokes told: {s.get('jokes', 0)}\n"
        f"☠︎︎ Stalkers Mephisto killed for you: {s.get('stalkers', 0)}\n\n"
        "*Mephisto has been watching...*"
    )