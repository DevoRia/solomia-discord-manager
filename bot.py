import sys
import discord

bot = discord.Client(intents=discord.Intents.all())
sys.modules[__name__] = bot
