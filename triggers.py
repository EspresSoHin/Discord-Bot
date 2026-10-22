import random

######################
#      Triggers      #
###################### 

async def handle_trigger(message, jokelist):

    content = message.content.lower()

    triggers = [
        (("patpat", "pat pat"), "*rubs against your hand*"),
        ("shoo", "*flies away*"),
        (("pspsps", "ps ps ps"), "Caw? *bonks head on you*"),
        ("caw", "*pecks your nose*"),
        ("boop", "Caw... *nuzzles you*"),
        ("flick", "*flapping his wings aggressively*"),
        ("boo!", "CAW! *hides behind Sylus*"),
        ("good night mephie", "*blinks eyes slowly and shuts down*"),
        ("good morning mephie", "!!! Morning Caw!!!"),
        ("mephie?", "*tilts head* Caw?"),
        ("good boy", "*puffs up proudly and does a little dance* Caw!"),
        ("bad boy", "*shakes blood off his wings and beak*"),
        ("i love you", "*hides face bashfully* Caw... ♡"),
    ]

    for command, response in triggers:
        if content.startswith(command):
            await message.channel.send(response)
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

    if "my boy" in content:
        await message.channel.send("*Mephisto nods cutely at you*")

    if "dance with sylus" in content:
        await message.channel.send("*Mephisto circles overhead like a backup dancer*")

    ###############   JSON Jokes    ###################

    if "tell me a crow joke" in content:
        joke = random.choice(jokelist["crow"])
        await message.channel.send(joke)

    if "tell me a kitten joke" in content:
        joke = random.choice(jokelist["kitten"])
        await message.channel.send(joke)

    if "tell me a joke, sylus" in content:
        joke = random.choice(jokelist["sylus"])
        await message.channel.send(joke)

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

    if "$commands" in content:
        await message.channel.send(
            "*Sylus voice in speaker:* Here are Mephisto's commands.\n\n patpat\n shoo\n pspsps\n caw\n boop\n flick\n boo!\n Good night Mephie\n Good morning Mephie\n Mephie?\n Good boy\n Bad boy\n I love you\n yay\n Badass trigger\n play boss.mp3\n Comfort me Mephie\n $Bubblewrap\n Tell me a crow joke\n Tell me a kitten joke\n Tell me a joke, Sylus\n Ask for a hug\n"
        )
