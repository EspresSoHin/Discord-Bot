import os
import database.postgres as db
from triggers import handle_trigger
from reminders import start_reminders
from games import start_games


WELCOME_GIF = "https://c.tenor.com/YlkdBVligYwAAAAd/tenor.gif"

# Handler (la "route")

def register_handlers(client):

    ##########################
    #      Join & Leave      #
    ##########################

    @client.event
    async def on_guild_join(guild):
        await db.add_server(guild.id, guild.name)


    @client.event
    async def on_guild_remove(guild):
        await db.remove_server(guild.id)
        await mongo.delete_stats(guild.id) #no ON CASCADE with noSQL, so do this


    ######################
    #   Welcome message  #
    ######################

    @client.event
    async def on_member_join(member):
        server = await db.get_server(member.guild.id)
        if server is None or not server["welcome_enabled"]:
            return

        channel_id = await db.get_channel(member.guild.id, "welcome")
        channel = member.guild.get_channel(channel_id) if channel_id else None
        if channel is None:
            return

        await channel.send(f"CAW CAW!!! Welcome to {member.guild.name}, {member.mention}\n\n{WELCOME_GIF}")

    #member.mention = f"<@{member.id}>"


    ######################
    #    Init triggers   #
    ######################

    @client.event
    async def on_message(message):
        if message.author.bot:
            return
        if message.guild is None:
            return

        await handle_trigger(message, client.jokelist)
        await start_games(message)