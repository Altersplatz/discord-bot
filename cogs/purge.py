import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self , client):
        self.client = client

    @commands.command(aliases=['clear'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self , ctx , amount=10):
        await ctx.channel.purge(limit=amount+1)

def setup(client):
    client.add_cog(Moderation(client))