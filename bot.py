import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def get_prefix(client, message):
    with open('./cogs/prefix_list.json', 'r') as f:
        prefixes = json.load(f)

    ID = str(message.guild.id)
    
    if ID not in prefixes:
        prefixes[ID] = '.'

        with open('./cogs/prefix_list.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    return prefixes[ID]

client = commands.Bot(command_prefix = get_prefix)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)