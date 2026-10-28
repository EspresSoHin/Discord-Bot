-- -----------------------------------------------------
-- Schema mephistobotdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS mephistobotdb;
SET search_path TO mephistobotdb;

-- -----------------------------------------------------
-- Table mephistobotdb.SERVERS
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mephistobotdb.servers (
  guild_id        BIGINT PRIMARY KEY,          -- ID Discord du serveur
  name            TEXT NOT NULL,
  welcome_message TEXT, --dropped for now, but could be used in the future
  welcome_enabled BOOLEAN NOT NULL DEFAULT TRUE,
  joined_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- -----------------------------------------------------
-- Table mephistobotdb.CHANNELS
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mephistobotdb.channels (
    id          SERIAL PRIMARY KEY,
    guild_id    BIGINT NOT NULL REFERENCES servers(guild_id) ON DELETE CASCADE,
    purpose     TEXT NOT NULL,                   -- 'welcome', 'general', 'qotd'...
    channel_id  BIGINT NOT NULL,
    UNIQUE (guild_id, purpose)
);

-- -----------------------------------------------------
-- Table mephistobotdb.ROLES
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mephistobotdb.roles (
    id          SERIAL PRIMARY KEY,
    guild_id    BIGINT NOT NULL REFERENCES servers(guild_id) ON DELETE CASCADE,
    purpose     TEXT NOT NULL,                   -- 'stamina', 'hunter'...
    role_id     BIGINT NOT NULL,
    UNIQUE (guild_id, purpose)
);

-- -----------------------------------------------------
-- Table mephistobotdb.REGIONS
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mephistobotdb.regions (
    id          SERIAL PRIMARY KEY,
    name        TEXT NOT NULL UNIQUE,            -- 'Asia', 'Europe', 'America'
    timezone    TEXT NOT NULL,                   -- 'Asia/Shanghai', 'Europe/Paris', 'America/Los_Angeles'
   reset_hour SMALLINT NOT NULL DEFAULT 5 CHECK (reset_hour BETWEEN 0 AND 23),
   reset_min  SMALLINT NOT NULL DEFAULT 0 CHECK (reset_min BETWEEN 0 AND 59)
);

-- -----------------------------------------------------
-- Table mephistobotdb.REMINDERS
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mephistobotdb.reminders (
    guild_id    BIGINT NOT NULL REFERENCES servers(guild_id) ON DELETE CASCADE,
    region_id   INT    NOT NULL REFERENCES regions(id),
    channel_id  BIGINT NOT NULL,
    role_id     BIGINT,
    enabled     BOOLEAN NOT NULL DEFAULT TRUE,
    PRIMARY KEY (guild_id, region_id)
);

INSERT INTO mephistobotdb.regions (name, timezone) VALUES
  ('Asia', 'Asia/Shanghai'),
  ('Europe', 'Europe/Paris'),
  ('America', 'America/Los_Angeles')
  ON CONFLICT (name) DO NOTHING;

------------------------------------------------------
--on delete cascade so if you remove the bot from the server, all the data is removed