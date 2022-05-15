import discord
from discord.ext import commands

class Information(commands.Cog):
    def __init__(self , client):
        self.client = client

    @commands.command()
    async def help(self , ctx):
        embed = discord.Embed(colour = discord.Colour.blue())

        embed.set_author(name = 'Help')
        embed.add_field(name = '>help' , value = 'Shows this message.' , inline = False)
        embed.add_field(name = '>ping' , value = 'Shows the bot\'s ping.' , inline = False)
        embed.add_field(name = '>kick' , value = 'Kicks a user.' , inline = False)
        embed.add_field(name = '>ban' , value = 'Bans a user.' , inline = False)
        embed.add_field(name = '>unban' , value = 'Unbans a user.' , inline = False)
        embed.add_field(name = '>clear' , value = 'Clears Recent 10 messages from a channel' , inline = False)

        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Information(client))