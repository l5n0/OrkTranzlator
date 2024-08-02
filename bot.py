import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from ork_language import translate_to_ork

# Load .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix='ç', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command(name='translate')
async def translate(ctx, *, text: str):
    translated_text = translate_to_ork(text)
    await ctx.send(translated_text)

bot.run(TOKEN)
