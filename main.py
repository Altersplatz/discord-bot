import discord
from discord.ext import commands

import os

client = commands.Bot(command_prefix = '>')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(">help"))
    print('Logged in as ' + client.user.name)

@client.event
async def on_command_error(ctx , error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing required argument.')
    elif isinstance(error, discord.ext.commands.errors.MissingPermissions) or isinstance(error , discord.Forbidden):
        await ctx.send('You do not have permission to use this command.')
    else:
        await ctx.send('An error has occured: ' + error)

@client.command()
async def load(extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('TOKEN')