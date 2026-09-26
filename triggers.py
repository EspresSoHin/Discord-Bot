import random
#add more random sentences to play boss.mp3

######################
#      Triggers      #
###################### 

async def handle_trigger(message):

    content = message.content.lower()

    if content.startswith("patpat"):
        await message.channel.send("*rubs against your hand*")

    if content.startswith("shoo"):
        await message.channel.send("*flies away*")

    if content.startswith("pspsps"):
        await message.channel.send("Caw? *bonks head on you*")

    if content.startswith("caw"):
        await message.channel.send("*pecks your nose*")

    if content.startswith("boop"):
        await message.channel.send("Caw... *nuzzles you*")

    if content.startswith("flick"):
        await message.channel.send("*flapping his wings aggressively*")

    if content.startswith("boo!"):
        await message.channel.send("CAW! *hides behind Sylus*")

    if content.startswith("good night mephie"):
        await message.channel.send("*blinks eyes slowly and shuts down*")

    if content.startswith("good morning mephie"):
        await message.channel.send("!!! Morning Caw!!!")

    if content.startswith("mephie?"):
        await message.channel.send("*tilts head* Caw?")

    if content.startswith("good boy"):
        await message.channel.send("*puffs up proudly and does a little dance* Caw!")

    if content.startswith("bad boy"):
        await message.channel.send("*shakes blood off his wings and beak*")

    if content.startswith("i love you"):
        await message.channel.send("*hides face bashfully* Caw... ♡")


    #############  Many commands, one reaction   ##################

    if any(phrase in content for phrase in [
        "may i have a hug",
        "can you give me a hug",
        "hug me mephie",
        "can i have a hug"
        "i need a hug"
]):
        await message.channel.send(
            "*Mephisto wraps his wings around you gently, "
            "providing a warm and comforting embrace*"
        )

    ###############   IF x IN    #####################

    if "hurts" in content:
        await message.channel.send("*looks sad* Caw... *brings you a little gem*")

    if "my boy" in content:
        await message.channel.send("*Mephisto nods cutely at you*")

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

    if "yay" in content:
        sticker = await message.guild.fetch_sticker(stickerID)
        await message.channel.send(stickers=[sticker]) 

    if "mephisto" in content:
        emoji = '<:mephie:1550153664486838332>'
        await message.add_reaction(emoji)

    if content.startswith("badass trigger"):
        await message.channel.send(
            "https://media.tenor.com/qfSDkr0lVSAAAAAM/merlo-uccelli.gif")


    ###############   Randomized reactions    ###################

    if "play boss.mp3" in content:
        await message.channel.send(
            "*Mephisto's speakers turn on* This is Sylus. Stay safe out there. And stop worrying about trivial matters, got it?"
        )


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
            "*Sylus voice in speaker:* Here are Mephisto's commands.\n\n patpat\n shoo\n pspsps\n caw\n boop\n flick\n boo!\n Good night Mephie\n Good morning Mephie\n Mephie?\n Good boy\n Bad boy\n I love you\n yay\n Badass trigger\n play boss.mp3\n Comfort me Mephie\n Bubblewrap!\n Tell me a crow joke\n Tell me a kitten joke\n Tell me a joke, Sylus\n May I have a hug?\n"
        )