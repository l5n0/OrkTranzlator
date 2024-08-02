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

class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="OrkTranzlator Bot Help", color=discord.Color.green())
        embed.add_field(name="çtl <text>", value="Translates the given text into Ork language.", inline=False)
        embed.add_field(name="Example", value="çtl Hello friends", inline=False)
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=f"{command.name} Command Help", color=discord.Color.green())
        embed.add_field(name=f"ç{command.name} {command.signature}", value=command.help, inline=False)
        await self.get_destination().send(embed=embed)

bot.help_command = CustomHelpCommand()

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command(name='tl', help='Translates the given text into Ork language.')
async def translate(ctx, *, text: str):
    translated_text = translate_to_ork(text)
    await ctx.send(translated_text)

bot.run(TOKEN)
