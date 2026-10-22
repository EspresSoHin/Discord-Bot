import discord
from discord import app_commands
import config_service as service

CHANNEL_CHOICES = [app_commands.Choice(name=p, value=p) for p in service.CHANNEL_PURPOSES]
ROLE_CHOICES = [app_commands.Choice(name=p, value=p) for p in service.ROLE_PURPOSES]


######################################################
#                  Command /config                   #
######################################################

def register_commands(tree: app_commands.CommandTree):

    config = app_commands.Group(
        name="config",
        description="Configure Mephisto for this server",
        guild_only=True,
    )

    #create the menu with the config commands. channel, role, welcome, show

######################################################
#                configure channels                  #
######################################################

    @config.command(name="channel", description="Choose a channel for a feature") #declare command
    @app_commands.checks.has_permissions(manage_guild=True)
    @app_commands.choices(purpose=CHANNEL_CHOICES) #roll menu with purposes
    
    async def config_channel(interaction: discord.Interaction,
                             purpose: app_commands.Choice[str],
                             channel: discord.TextChannel):
        can_send = channel.permissions_for(interaction.guild.me).send_messages #mais il s'appelle bot_can_send dans le service?
        msg = await service.set_channel(interaction.guild_id, purpose.value, channel.id, can_send)
        await interaction.response.send_message(msg, ephemeral=True)

######################################################
#             configure roles to ping                #
######################################################
    
    @config.command(name="role", description="Choose a role to ping for a feature")
    @app_commands.checks.has_permissions(manage_guild=True)
    @app_commands.choices(purpose=ROLE_CHOICES)
    
    async def config_role(interaction: discord.Interaction,
                          purpose: app_commands.Choice[str],
                          role: discord.Role):
        msg = await service.set_role(interaction.guild_id, purpose.value, role.id)
        await interaction.response.send_message(msg, ephemeral=True)

######################################################
#                set welcome message                 #
######################################################
    
    @config.command(name="welcome", description="Turn welcome messages on or off")
    @app_commands.checks.has_permissions(manage_guild=True)
    
    async def config_welcome(interaction: discord.Interaction, enabled: bool):
        msg = await service.set_welcome(interaction.guild_id, enabled)
        await interaction.response.send_message(msg, ephemeral=True)

######################################################
#               Unset channels & roles               #
######################################################

    @config.command(name="unset-channel", description="Remove a channel setting")
    @app_commands.checks.has_permissions(manage_guild=True)
    @app_commands.choices(purpose=CHANNEL_CHOICES)
    async def config_unset_channel(interaction: discord.Interaction,
                                purpose: app_commands.Choice[str]):
        msg = await service.unset_channel(interaction.guild_id, purpose.value)
        await interaction.response.send_message(msg, ephemeral=True)


    @config.command(name="unset-role", description="Remove a role setting")
    @app_commands.checks.has_permissions(manage_guild=True)
    @app_commands.choices(purpose=ROLE_CHOICES)
    async def config_unset_role(interaction: discord.Interaction,
                                purpose: app_commands.Choice[str]):
        msg = await service.unset_role(interaction.guild_id, purpose.value)
        await interaction.response.send_message(msg, ephemeral=True)


######################################################
#                final config recap                  #
######################################################
    
    @config.command(name="show", description="Show this server's configuration")
    @app_commands.checks.has_permissions(manage_guild=True)
    
    async def config_show(interaction: discord.Interaction):
        msg = await service.show_config(interaction.guild_id)
        await interaction.response.send_message(msg, ephemeral=True)

    tree.add_command(config)




    @tree.error
    async def on_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(
                "Caw?! You need the **Manage Server** permission for that.", ephemeral=True)
        else:
            raise error