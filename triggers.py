import random
from service import stats_service as stats

######################
#      Triggers      #
###################### 

async def handle_trigger(message, jokelist):

    content = message.content.lower()

    triggers = [
        (("patpat", "pat pat"), "*rubs against your hand*", "pats"),
        ("shoo", "*flies away*", None),
        (("pspsps", "ps ps ps"), "Caw? *bonks head on you*", None),
        ("caw", "*pecks your nose*", "caw"),
        ("boop", "Caw... *nuzzles you*", None),
        ("flick", "*flapping his wings aggressively*", None),
        ("boo!", "CAW! *hides behind Sylus*", None),
        ("good night mephie", "*blinks eyes slowly and shuts down*", None),
        ("good morning mephie", "!!! Morning Caw!!!", None),
        ("mephie?", "*tilts head* Caw?", None),
        ("good boy", "*puffs up proudly and does a little dance* Caw!", None),
        ("bad boy", "*shakes blood off his wings and beak*", None),
        ("i love you", "*hides face bashfully* Caw... ♡", None),
    ]

    for command, response, counter in triggers:
        if content.startswith(command):
            await message.channel.send(response)
            if counter:
                await stats.record(message.guild.id, counter)
            break

    #############  Many commands, one reaction   ##################

    if any(phrase in content for phrase in [ 
        "may i have a hug",
        "can you give me a hug",
        "hug me mephie",
        "can i have a hug",
        "i need a hug",
        "give me a hug"
]):
        await message.channel.send(
            "*Mephisto wraps his wings around you gently, providing a warm and comforting embrace*"
        )


    ###############   IF x IN    #####################

    if "hurts" in content:
        await message.channel.send("*looks sad* Caw... *brings you a little gem*")
        await stats.record(message.guild.id, "gems")

    if "my boy" in content:
        await message.channel.send("*Mephisto nods cutely at you*")

    if "dance with sylus" in content:
        await message.channel.send("*Mephisto circles overhead like a backup dancer*")

    ###############   JSON Jokes    ###################

    if "tell me a crow joke" in content:
        joke = random.choice(jokelist["crow"])
        await message.channel.send(joke)
        await stats.record(message.guild.id, "jokes")

    if "tell me a kitten joke" in content:
        joke = random.choice(jokelist["kitten"])
        await message.channel.send(joke)
        await stats.record(message.guild.id, "jokes")

    if "tell me a joke, sylus" in content:
        joke = random.choice(jokelist["sylus"])
        await message.channel.send(joke)
        await stats.record(message.guild.id, "jokes")

    ###############   Non-text reactions    ###################

    #if "yay" in content:
        #sticker = await message.guild.fetch_sticker(stickerID)
        #await message.channel.send(stickers=[sticker]) #voir pour le sticker
    
    #YAY_STICKERS = {
    #SERVER_ID_1: ID_SERVER_STICKER_1,
    #SERVEUR_ID_2: ID_SERVER_STICKER_2}

    #if "yay" in content:
        #sticker_id = YAY_STICKERS.get(message.guild.id)

        #if sticker_id is not None:
            #sticker = await message.guild.fetch_sticker(sticker_id)
            #await message.channel.send(stickers=[sticker])


    if "mephisto" in content:
        emoji = '<:mephie:1550153664486838332>'
        await message.add_reaction(emoji)

    if "badass trigger" in content:
        await message.channel.send(
            "https://media.tenor.com/qfSDkr0lVSAAAAAM/merlo-uccelli.gif")


    ###############   Randomized reactions    ###################

    if "play boss.mp3" in content:
        await message.channel.send(
            "*Mephisto's speakers turn on* This is Sylus. Stay safe out there. And stop worrying about trivial matters, got it?"
        ) #add more random sentences to play boss.mp3


    if content.startswith("comfort me mephie"):
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

    ###############   Commands    ###################

    if content.startswith("$mephisto"):
        await message.channel.send(await stats.mephisto_report(message.guild.id))

    if "$commands" in content:
        lines = [
            "*Sylus voice in speaker:* Here are Mephisto's commands.", "",
            "patpat", "shoo", "pspsps", "caw", "boop", "flick", "boo!",
            "Good night Mephie", "Good morning Mephie", "Mephie?",
            "Good boy", "Bad boy", "I love you",
            "Badass trigger", "play boss.mp3", "Comfort me Mephie",
            "Tell me a crow joke", "Tell me a kitten joke", "Tell me a joke, Sylus",
            "Ask for a hug", "$mephisto", "$Bubblewrap", #yay sticker
        ]
        await message.channel.send("\n".join(lines))