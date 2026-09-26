import discord
import requests
import json
from triggers import handle_trigger
from reminders import start_reminders
from games import start_games


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)


#########################
#     Initialisation    #
#         du bot        #
#########################


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await handle_trigger(message)
    await start_games(message)



@client.event
async def on_ready():
    global jokelist

    print(f"We have logged in as {client.user}")

    channel = client.get_channel(botchannelID)
    await channel.send("Mephisto has awoken.")

    response = requests.get(
        "https://raw.githubusercontent.com/EspresSoHin/Discord-Bot/refs/heads/Develop/crowkittenjokes.json"
    )
    jokelist = response.json()

    start_reminders(client)



######################
#   Welcome message  #
######################


@client.event
async def on_member_join(member):
    channel = client.get_channel(welcomechannelID)
    await channel.send(f"CAW CAW!!! (Welcome to the server!), <@{member.id}> \n\n https://c.tenor.com/YlkdBVligYwAAAAd/tenor.gif")




client.run("TOKEN")


###############
#    Notes    #
###############

#tagguer roles <@&roleID>
#tagguer channel <#CHANNEL_ID>
#tagguer membre <@userID>