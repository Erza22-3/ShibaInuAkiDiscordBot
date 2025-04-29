
import os
from dotenv import load_dotenv
import discord
from discord import app_commands

# Load environment variables
load_dotenv()

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True
intents.voice_states = True  # Add voice state intent for voice channel detection

client = discord.Client(intents=intents, reconnect=True)
tree = app_commands.CommandTree(client)

TOKEN = os.getenv("TOKEN")
