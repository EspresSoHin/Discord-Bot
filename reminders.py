from discord.ext import tasks
from zoneinfo import ZoneInfo
import datetime

client = None

##########################
#  Water Daily Reminder  #
##########################

sent_today = False

@tasks.loop(seconds=10)
async def send_at_time():
    global sent_today

    now = datetime.datetime.now()

    if now.hour == 17 and now.minute == 30:
        if not sent_today:
            print("TASK TRIGGERED")

            channel = client.get_channel(generalID)
            if channel:
                await channel.send("*Mephisto pushes a water bottle towards you with his beak.* Caw caw! ")

            sent_today = True
    else:
        sent_today = False


############################
#  Stamina Bottle Reminder #
############################

sent_this_week = False

@tasks.loop(seconds=10)
async def send_at_time_weekly():
    global sent_this_week 

    now = datetime.datetime.now()

    if now.weekday() == 5 and now.hour == 22 and now.minute == 30:
        if not sent_this_week:
            print("WEEKLY TASK TRIGGERED")

            channel = client.get_channel(generalID)
            if channel:
                await channel.send("*Mephisto knocks on your window carrying stamina bottles. Alarms are blearing through his wings.* <@&roleID>, <:stamina:1550225208546295908> Caw <:stamina:1550225208546295908> Caw!<:stamina:1550225208546295908>")

            sent_this_week = True
    else:
        sent_this_week = False



#########################
#    QOTD Reminder      #
#########################

sent_today_qotd = False
@tasks.loop(seconds=10)
async def send_at_time_qotd():
    global sent_today_qotd

    now = datetime.datetime.now(ZoneInfo("America/New_York"))

    qotdchannels = [
    client.get_channel(channelID), 
    client.get_channel(channelID), 
    client.get_channel(channelID) 
]

    if now.hour == 1 and now.minute == 15:
        if not sent_today_qotd:
            print("QOTD TASK TRIGGERED")

            for channel in qotdchannels:
                if channel:
                    await channel.send("CAW!! Caw caw caw!! *Sylus voice in Mephisto's speakers:* Kittens, Question of the day dropped at <#1526731037357641840>. Don't be late. \n\n Come on kitten, clock is ticking...")

            sent_today_qotd = True
    else:
        sent_today_qotd = False



#########################
#    Pour ajouter un    #
# prochain reminder/test#
#########################

sent_today_test = False
@tasks.loop(seconds=10)
async def send_at_time_test():
    global sent_today_test

    now = datetime.datetime.now()

    if now.hour == 17 and now.minute == 30: #UTC+3
        if not sent_today_test:
            print("TEST TASK TRIGGERED")

            channel = client.get_channel(channelID)
            if channel:
                await channel.send("*Sylus voice in Mephisto's speakers:* Sohin, that's enough. Mephisto needs to rest.")

            sent_today_test = True
    else:
        sent_today_test = False


def start_reminders(bot_client):
    global client
    client = bot_client

    send_at_time.start()
    send_at_time_weekly.start()
    send_at_time_qotd.start()
    send_at_time_test.start()