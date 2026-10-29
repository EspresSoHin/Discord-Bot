import os
import asyncpg


pool: asyncpg.Pool | None = None

async def init_pool():
    global pool
    pool = await asyncpg.create_pool(
        os.environ["DATABASE_URL"],
        statement_cache_size=0,
        min_size=1,
        max_size=5,
    )

"SELECT channel_id FROM mephistobotdb.channels WHERE guild_id = $1 AND purpose = $2"

##########################################################################################################################
# -------------------------------------------------- Servers ------------------------------------------------------------#
##########################################################################################################################


async def add_server(guild_id: int, name: str):
    await pool.execute(
        """INSERT INTO mephistobotdb.servers (guild_id, name) VALUES ($1, $2)
           ON CONFLICT (guild_id) DO UPDATE SET name = EXCLUDED.name""",
        guild_id, name)

async def remove_server(guild_id: int):
    await pool.execute("DELETE FROM mephistobotdb.servers WHERE guild_id = $1", guild_id)

async def get_server(guild_id: int):
    return await pool.fetchrow("SELECT * FROM mephistobotdb.servers WHERE guild_id = $1", guild_id)


##########################################################################################################################
# ----------------------------------------- Setup of channels and role --------------------------------------------------#
##########################################################################################################################


async def set_welcome_enabled(guild_id: int, enabled: bool):
    await pool.execute(
        "UPDATE mephistobotdb.servers SET welcome_enabled = $2 WHERE guild_id = $1",
        guild_id, enabled)

async def get_channels(guild_id: int):
    return await pool.fetch(
        "SELECT purpose, channel_id FROM mephistobotdb.channels WHERE guild_id = $1 ORDER BY purpose",
        guild_id)

async def get_roles(guild_id: int):
    return await pool.fetch(
        "SELECT purpose, role_id FROM mephistobotdb.roles WHERE guild_id = $1 ORDER BY purpose",
        guild_id)


##########################################################################################################################
# ------------------------------------------ Channels / Roles by Usage --------------------------------------------------#
##########################################################################################################################


async def set_channel(guild_id: int, purpose: str, channel_id: int):
    await pool.execute(
        """INSERT INTO mephistobotdb.channels (guild_id, purpose, channel_id) VALUES ($1, $2, $3)
           ON CONFLICT (guild_id, purpose) DO UPDATE SET channel_id = EXCLUDED.channel_id""",
        guild_id, purpose, channel_id)

async def get_channel(guild_id: int, purpose: str) -> int | None:
    return await pool.fetchval(
        "SELECT channel_id FROM mephistobotdb.channels WHERE guild_id = $1 AND purpose = $2",
        guild_id, purpose)

async def set_role(guild_id: int, purpose: str, role_id: int):
    await pool.execute(
        """INSERT INTO mephistobotdb.roles (guild_id, purpose, role_id) VALUES ($1, $2, $3)
           ON CONFLICT (guild_id, purpose) DO UPDATE SET role_id = EXCLUDED.role_id""",
        guild_id, purpose, role_id)

async def get_role(guild_id: int, purpose: str) -> int | None:
    return await pool.fetchval(
        "SELECT role_id FROM mephistobotdb.roles WHERE guild_id = $1 AND purpose = $2",
        guild_id, purpose)


##########################################################################################################################
# ------------------------------------------------- Set yay stickers ----------------------------------------------------#
##########################################################################################################################


async def set_reaction_sticker(guild_id: int, sticker_id: int | None):
    await pool.execute(
        "UPDATE mephistobotdb.servers SET reaction_sticker_id = $2 WHERE guild_id = $1",
        guild_id, sticker_id)

async def get_reaction_sticker(guild_id: int) -> int | None:
    return await pool.fetchval(
        "SELECT reaction_sticker_id FROM mephistobotdb.servers WHERE guild_id = $1",
        guild_id)


##########################################################################################################################
# --------------------------------------------- Delete channels & roles -------------------------------------------------#
##########################################################################################################################


async def delete_channel(guild_id: int, purpose: str) -> bool:
    deleted = await pool.fetchval(
        """DELETE FROM mephistobotdb.channels WHERE guild_id = $1 AND purpose = $2 RETURNING id""",
        guild_id, purpose)
    return deleted is not None

async def delete_role(guild_id: int, purpose: str) -> bool:
    deleted = await pool.fetchval(
        """DELETE FROM mephistobotdb.roles WHERE guild_id = $1 AND purpose = $2 RETURNING id""",
        guild_id, purpose)
    return deleted is not None


##########################################################################################################################
# --------------------------------------------- Reminders per timezone --------------------------------------------------#
##########################################################################################################################

async def get_all_reminders():
    return await pool.fetch(
        """SELECT r.guild_id, r.channel_id, r.role_id, g.name, g.timezone, g.reset_hour, g.reset_min
           FROM mephistobotdb.reminders r JOIN mephistobotdb.regions g ON g.id = r.region_id
           WHERE r.enabled""")


async def get_guild_reminders(guild_id: int):
    return await pool.fetch(
        """SELECT g.name, r.channel_id, r.role_id
           FROM mephistobotdb.reminders r JOIN mephistobotdb.regions g ON g.id = r.region_id
           WHERE r.guild_id = $1 AND r.enabled
           ORDER BY g.name""",
        guild_id)


##########################################################################################################################
# --------------------------------------------------- Reminders ---------------------------------------------------------#
##########################################################################################################################

async def get_region_by_name(name: str):
    return await pool.fetchrow(
        "SELECT * FROM mephistobotdb.regions WHERE name = $1", name)

async def set_reminder(guild_id: int, region_id: int, channel_id: int, role_id: int | None):
    await pool.execute(
        """INSERT INTO mephistobotdb.reminders (guild_id, region_id, channel_id, role_id)
           VALUES ($1, $2, $3, $4)
           ON CONFLICT (guild_id, region_id)
           DO UPDATE SET channel_id = EXCLUDED.channel_id, role_id = EXCLUDED.role_id, enabled = TRUE""",
        guild_id, region_id, channel_id, role_id)

async def delete_reminder(guild_id: int, region_id: int) -> bool:
    deleted = await pool.fetchval(
        """DELETE FROM mephistobotdb.reminders WHERE guild_id = $1 AND region_id = $2 RETURNING region_id""",
        guild_id, region_id)
    return deleted is not None


##########################################################################################################################
# ------------------------------------- Servers with reminders and their roles ------------------------------------------#
##########################################################################################################################

async def get_reminder_targets(purpose: str):
    return await pool.fetch(
        """SELECT c.guild_id, c.channel_id, r.role_id
           FROM mephistobotdb.channels c
           LEFT JOIN mephistobotdb.roles r
                  ON r.guild_id = c.guild_id AND r.purpose = c.purpose
           WHERE c.purpose = $1""",
        purpose)