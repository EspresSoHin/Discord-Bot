import database.postgres as db

CHANNEL_PURPOSES = ["welcome", "general", "daily", "weekly"]
ROLE_PURPOSES = ["weekly"] #"reminders", "all"

##################################
#   Choose a channel and check   #
#    if Mephie can talk in it    #
##################################

async def set_channel(guild_id: int, purpose: str, channel_id: int, bot_can_send: bool) -> str:
    if purpose not in CHANNEL_PURPOSES:
        return "Caw? I don't know that channel purpose..."
    if not bot_can_send:
        return "Caw! I can't send messages in that channel, CAW! Give me the permission first!"
    await db.set_channel(guild_id, purpose, channel_id)
    return f"CAW CAW! **{purpose}** channel is now <#{channel_id}>."


##################################
#     Choose a role and give     #
#     it a purpose for pings     #
##################################

async def set_role(guild_id: int, purpose: str, role_id: int) -> str:
    if purpose not in ROLE_PURPOSES:
        return "Caw? I don't know that role purpose..."
    await db.set_role(guild_id, purpose, role_id)
    return f"Caw! **{purpose}** role is now <@&{role_id}>."


##################################
#   Get the welcome channel and  # 
#  check if it's enabled or not  #
##################################

async def set_welcome(guild_id: int, enabled: bool) -> str:
    await db.set_welcome_enabled(guild_id, enabled)
    return "Welcome messages are now **on**." if enabled else "Welcome messages are now **off**."


##################################
#      Remove channel & role     #
#           from config          #
##################################

async def unset_channel(guild_id: int, purpose: str) -> str:
    removed = await db.delete_channel(guild_id, purpose)
    if removed:
        return f"**{purpose}** channel has been removed, Caw!"
    return f"Caw? There was no **{purpose}** channel set."


async def unset_role(guild_id: int, purpose: str) -> str:
    removed = await db.delete_role(guild_id, purpose)
    if removed:
        return f"**{purpose}** role has been removed, Caw!"
    return f"Caw? There was no **{purpose}** role set."


##################################
#  Set & unset of the reminders  #
##################################

async def set_reset_reminder(guild_id: int, region_name: str, channel_id: int,
                             role_id: int | None, bot_can_send: bool) -> str:
    region = await db.get_region_by_name(region_name)
    if region is None:
        return "Caw? I don't know that region."
    if not bot_can_send:
        return "Caw! I can't send messages in that channel. Give me the permission first!"
    await db.set_reminder(guild_id, region["id"], channel_id, role_id)
    return f"Caw! **{region_name}** reset reminder will be sent in <#{channel_id}>."


async def unset_reset_reminder(guild_id: int, region_name: str) -> str:
    region = await db.get_region_by_name(region_name)
    if region is None:
        return "Caw? I don't know that region."
    removed = await db.delete_reminder(guild_id, region["id"])
    if removed:
        return f"**{region_name}** reset reminder has been removed, Caw caw!."
    return f"Caw? There was no **{region_name}** reset reminder."


##################################
#    Final configuration check   #
#          and recap yay         #
##################################

async def show_config(guild_id: int) -> str:
    channels = await db.get_channels(guild_id)
    roles = await db.get_roles(guild_id)
    server = await db.get_server(guild_id)

    lines = [f"**Welcome messages:** {'on' if server['welcome_enabled'] else 'off'}", "", "**Channels**"]
    lines += [f"- {c['purpose']}: <#{c['channel_id']}>" for c in channels] or ["- none set"]
    lines += ["", "**Roles**"]
    lines += [f"- {r['purpose']}: <@&{r['role_id']}>" for r in roles] or ["- none set"]
    return "\n".join(lines)
