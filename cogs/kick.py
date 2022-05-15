import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self , client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self , ctx , member: discord.Member , * , reason = None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked user for {reason}')

def setup(client):
    client.add_cog(Moderation(client))