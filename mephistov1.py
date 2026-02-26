import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    channel = client.get_channel(1459950649427886295)
    await channel.send("Mephisto has awoken.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("patpat"):
        await message.channel.send("*rubs against your hand*")

    if message.content.startswith("shoo"):
        await message.channel.send("*flies away*")

    if message.content.startswith("pspsps"):
        await message.channel.send("Caw? *bonks head on you*")

    if message.content.startswith("caw"):
        await message.channel.send("*pecks your nose*")

    if message.content.startswith("boop"):
        await message.channel.send("Caw... *nuzzles you*")

    if message.content.startswith("flick"):
        await message.channel.send("*flapping his wings aggressively*")

    if message.content.startswith("boo!"):
        await message.channel.send("CAW! *hides behind Sylus*")

    if message.content.startswith("Good night Mephie"):
        await message.channel.send("*blinks eyes slowly and shuts down*")

    if message.content.startswith("Good morning Mephie"):
        await message.channel.send("!!! Morning Caw!!!	")

    if message.content.startswith("Mephie?"):
        await message.channel.send("*tilts head* Caw?")

    if message.content.startswith("Good boy"):
        await message.channel.send("*puffs up proudly and does a little dance* Caw!")

    if message.content.startswith("Bad boy"):
        await message.channel.send("*shakes blood off his wings and beak*")

    if message.content.startswith("I love you"):
        await message.channel.send("*hides face bashfully* Caw... ♡")

    if message.content.startswith("Badass trigger"):
        await message.channel.send(
            "https://images-ext-1.discordapp.net/external/PlFF4m9k4UtMs7Obbztrmc5YyOuq3rodXgNMMfC7hQ8/https/media.tenor.com/qfSDkr0lVSAAAAPo/merlo-uccelli.mp4"
        )

    if "hurts" in message.content:
        await message.channel.send("*looks sad* Caw... *brings you a little gem*")

    if "play boss.mp3" in message.content:
        await message.channel.send(
            "*Mephisto's speakers turn on* This is Sylus. Stay safe out there. And stop worrying about trivial matters, got it?"
        )

    if "my boy" in message.content:
        await message.channel.send("*Mephisto nods cutely at you*")

    if message.content.startswith("Comfort me Mephie"):
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

    if "!commands" in message.content:
        await message.channel.send(
            "*Sylus voice in speaker:* Here are Mephisto's commands.\n\n patpat\n shoo\n flies away\n pspsps\n bonks head on you\n caw\n boop\n flick\n boo!\n Good night Mephie\n Good morning Mephie\n Mephie\n Good boy\n Bad boy\n I love you\n Badass trigger\n hurts\n play boss.mp3\n my boy\n Comfort me Mephie"
        )


client.run("token")
