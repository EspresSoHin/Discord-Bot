import discord
from discord.ext import tasks
from zoneinfo import ZoneInfo
import datetime
import database.postgres as db

client = None


# Wispbyte server time UTC+3
SERVER_TZ = datetime.timezone(datetime.timedelta(hours=3))


#########################
#  reminders safe init  #
#########################

    # If one channel has an error, prevents from crashing on all servers

async def safe_send(channel, text: str):
    try:
        await channel.send(text)
    except (discord.Forbidden, discord.HTTPException) as e:
        print(f"Reminder not sent in channel {channel.id}: {e}")


async def send_to_targets(purpose: str, text: str):
    for row in await db.get_reminder_targets(purpose):
        channel = client.get_channel(row["channel_id"])
        if channel is None:
            continue
        ping = f"<@&{row['role_id']}> " if row["role_id"] else ""
        await safe_send(channel, ping + text)


##########################
#  Water Daily Reminder  #
##########################

@tasks.loop(time=datetime.time(hour=17, minute=30, tzinfo=SERVER_TZ))
async def water_reminder():
    await send_to_targets(
        "daily",
        "*Mephisto pushes a water bottle towards you with his beak.* Caw caw!")


############################
#  Stamina Weekly Reminder #
############################

@tasks.loop(time=datetime.time(hour=22, minute=30, tzinfo=SERVER_TZ))
async def stamina_reminder():
    if datetime.datetime.now(SERVER_TZ).weekday() == 5:   # saturday
        await send_to_targets(
            "weekly",
            "*Mephisto knocks on your window carrying stamina bottles. Alarms are blearing through his wings.* "
            "<:stamina:1550225208546295908> Caw <:stamina:1550225208546295908> Caw! "
            "<:stamina:1550225208546295908>")


#########################
#    Servers Reset      #
#########################

@tasks.loop(minutes=1)
async def reset_reminders():
    for r in await db.get_all_reminders():
        now = datetime.datetime.now(ZoneInfo(r["timezone"]))
        
        if now.hour == r["reset_hour"] and now.minute == r["reset_min"]:
            channel = client.get_channel(r["channel_id"])
            if channel is None:
                continue
            ping = f"<@&{r['role_id']}> " if r["role_id"] else ""
            await safe_send(
                channel,
                f"{ping}*Mephisto preens his feathers and hits the speakers.* Caw! The **{r['name']}** server reset is now CAW!")





def start_reminders(bot_client):
    global client
    client = bot_client
    for task in (water_reminder, stamina_reminder, reset_reminders):
        if not task.is_running():
            task.start()

