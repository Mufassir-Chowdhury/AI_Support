import discord
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over cseians 👀"))
        print(f'{self.client.user.name} has connected to Discord!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(f'Hi {member.name}, welcome to our Discord Community!')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if "shut up" in message.content:
            await message.channel.send(f'you shut up! {message.author.mention}')
        if "69" in message.content:
            await message.channel.send("96!")
        if  "fuck" in message.content:
            await message.channel.send(f'Hol ON! {message.author.mention}')

def setup(client):
    client.add_cog(Events(client))