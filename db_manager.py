
from replit import db

def get_setting(guild_id, setting_name, default=None):
    key = f"guild_{guild_id}_{setting_name}"
    return db.get(key, default)

def set_setting(guild_id, setting_name, value):
    key = f"guild_{guild_id}_{setting_name}"
    db[key] = value

def get_all_guild_settings(guild_id):
    prefix = f"guild_{guild_id}_"
    return {key.replace(prefix, ""): db[key] for key in db.prefix(prefix)}
