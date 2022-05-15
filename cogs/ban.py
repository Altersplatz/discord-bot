import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self , client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self , ctx , member: discord.Member , * , reason = None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} for {reason}')

def setup(client):
    client.add_cog(Moderation(client))