# Created by OLuke-dot on gitHub
from discord.ext import commands
import os

client = commands.Bot(command_prefix='!')
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.channel.send(f'loaded {extension}.py...')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.channel.send(f'unloaded {extension}.py...')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.channel.send(f'reloaded {extension}.py...')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Bot is working with latency {round(client.latency *1000)}ms') # Can personalize 
    # command for pinging

for fname in os.listdir('C:\\Users\\lukek\\OneDrive\\Python\\Pawlacz_bot\\cogs'):
    if fname.endswith('.py'):
        client.load_extension(f'cogs.{fname[:-3]}')
client.run(' ') # Insert your key here
