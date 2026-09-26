import discord
import random
from discord.ext import tasks
import datetime
import requests
import json
from zoneinfo import ZoneInfo #added

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

##########################
#  WATER DAILY REMINDER  #
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
#  REMINDER STAMINA BOTTLE #
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
#         QOTD          #
#########################

sent_today_qotd = False
@tasks.loop(seconds=10)
async def send_at_time_qotd():
    global sent_today_qotd

    now = datetime.datetime.now(ZoneInfo("America/New_York"))

    qotdchannels = [
    client.get_channel(1524597999974486320), #general
    client.get_channel(1525223630349402242), #og5only
    client.get_channel(1542368348208107594) #forwarding
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

    if now.hour == 17 and now.minute == 30: #ou autre heure avec toujours 1heure plus tard que la vraie heure
        if not sent_today_test:
            print("TEST TASK TRIGGERED")

            channel = client.get_channel(channelID)
            if channel:
                await channel.send("*Sylus voice in Mephisto's speakers:* Sohin, that's enough. Mephisto needs to rest.")

            sent_today_test = True
    else:
        sent_today_test = False


#########################
#     Initialisation    #
#         du bot        #
#########################


@client.event
async def on_ready():
    global jokelist
    print(f"We have logged in as {client.user}")
    channel = client.get_channel(botchannelID)
    await channel.send("Mephisto has awoken.")
    send_at_time.start()
    send_at_time_weekly.start()
    sent_at_time_qotd.start() #added
    send_at_time_test.start()  #TEST
    response = requests.get("https://raw.githubusercontent.com/EspresSoHin/Discord-Bot/refs/heads/Develop/crowkittenjokes.json") #added
    jokelist = response.json()


######################
#       Welcome      #
#       message      #
######################


@client.event
async def on_member_join(member):
    channel = client.get_channel(welcomechannelID)
    await channel.send(f"CAW CAW!!! (Welcome to the server!), <@{member.id}> \n\n https://c.tenor.com/YlkdBVligYwAAAAd/tenor.gif")


######################
#      Triggers      #
######################

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("patpat"):
        await message.channel.send("*rubs against your hand*")

    if message.content.lower().startswith("shoo"):
        await message.channel.send("*flies away*")

    if message.content.lower().startswith("pspsps"):
        await message.channel.send("Caw? *bonks head on you*")

    if message.content.lower().startswith("caw"):
        await message.channel.send("*pecks your nose*")

    if message.content.lower().startswith("boop"):
        await message.channel.send("Caw... *nuzzles you*")

    if message.content.lower().startswith("flick"):
        await message.channel.send("*flapping his wings aggressively*")

    if message.content.lower().startswith("boo!"):
        await message.channel.send("CAW! *hides behind Sylus*")

    if message.content.lower().startswith("good night mephie"):
        await message.channel.send("*blinks eyes slowly and shuts down*")

    if message.content.lower().startswith("good morning mephie"):
        await message.channel.send("!!! Morning Caw!!!")

    if message.content.lower().startswith("mephie?"):
        await message.channel.send("*tilts head* Caw?")

    if message.content.lower().startswith("good boy"):
        await message.channel.send("*puffs up proudly and does a little dance* Caw!")

    if message.content.lower().startswith("bad boy"):
        await message.channel.send("*shakes blood off his wings and beak*")

    if message.content.lower().startswith("i love you"):
        await message.channel.send("*hides face bashfully* Caw... ♡")

    if "hurts" in message.content.lower():
        await message.channel.send("*looks sad* Caw... *brings you a little gem*")
        
    if "yay" in message.content.lower():
        sticker = await message.guild.fetch_sticker(stickerID)
        await message.channel.send(stickers=[sticker]) 

    if "mephisto" in message.content.lower():
        emoji = '<:mephie:1550153664486838332>'
        await message.add_reaction(emoji)

    if message.content.lower().startswith("badass trigger"):
        await message.channel.send(
            "https://media.tenor.com/qfSDkr0lVSAAAAAM/merlo-uccelli.gif"
        )

    if "play boss.mp3" in message.content.lower():
        await message.channel.send(
            "*Mephisto's speakers turn on* This is Sylus. Stay safe out there. And stop worrying about trivial matters, got it?"
        )

    if "my boy" in message.content.lower():
        await message.channel.send("*Mephisto nods cutely at you*")

    if message.content.lower().startswith("comfort me mephie"):
        reponses = [
            "Caw! You are the best, Caw!!",
            "You are a cawderful person, Cawcaw!",
            "*flaps wings excitedly at your beauty*",
            "*looks around for things that can make you falter. He finds nothing*",
            "Caw caw... *nuzzles against you because you're soft and warm*",
            "*Mephisto's speakers turn on, revealing Sylus'voice* You are doing amazing, sweetie.",
            "... *Mephisto looks at you with glowing red eyes. He desires revenge against those who hurt you*",
            "?? !! *Mephisto is so excited to see you that he can't even form caws!*",
            "Caw. Caw. Caw. Caw. Caw. Caw. Caw. Caw. Caw. *Mephisto is counting the gems he has collected for each of your accomplishments. He fell asleep, there are too many!*",
        ]
        answer = random.choice(reponses)
        await message.channel.send(answer)

    if message.content.lower().startswith("bubblewrap!"):
        bubbles = ["||pffft||", "||POP||"]
        secret_bubble1 = "||♡♡♡||"
        secret_bubble2 = "||CAW||"

        grid = [[random.choice(bubbles) for _ in range(10)] for _ in range(16)]

    
        row_caw, col_caw = random.randint(0, 15), random.randint(0, 9)
        row_heart, col_heart = random.randint(0, 15), random.randint(0, 9)

   
        while (row_caw, col_caw) == (row_heart, col_heart):
            row_heart, col_heart = random.randint(0, 15), random.randint(0, 9)

   
        grid[row_caw][col_caw] = secret_bubble2
        grid[row_heart][col_heart] = secret_bubble1

    
        bubble_wrap = "\n".join(" ".join(row) for row in grid)

        await message.channel.send(bubble_wrap)


    if "tell me a crow joke" in message.content.lower():
        joke = random.choice(jokelist["crow"])
        await message.channel.send(joke)

    if "tell me a kitten joke" in message.content.lower():
        joke = random.choice(jokelist["kitten"])
        await message.channel.send(joke)

    if "tell me a joke, sylus" in message.content.lower():
        joke = random.choice(jokelist["sylus"])
        await message.channel.send(joke)

    if "may i have a hug?" in message.content.lower(): #or can you give me a hug? a voir 
        await message.channel.send("*Mephisto wraps his wings around you gently, providing a warm and comforting embrace*")

    if "$commands" in message.content.lower():
        await message.channel.send(
            "*Sylus voice in speaker:* Here are Mephisto's commands.\n\n patpat\n shoo\n pspsps\n caw\n boop\n flick\n boo!\n Good night Mephie\n Good morning Mephie\n Mephie?\n Good boy\n Bad boy\n I love you\n Badass trigger\n hurts\n play boss.mp3\n my boy\n Comfort me Mephie\n Bubblewrap!\n Tell me a crow joke\n Tell me a kitten joke\n Tell me a joke, Sylus\n May I have a hug?\n"
        )


client.run("token")


###############
#    Notes    #
###############

#tagguer roles <@&roleID>
#tagguer channel <#CHANNEL_ID>
#tagguer membre <@userID>
