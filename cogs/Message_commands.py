import discord
from discord.ext import commands

class mComms(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms!')

    @commands.command()
    async def classes(self, ctx):
        await ctx.send(
                '1/2\n'
                '#Mon__19_10_20\n'
                'DS137 class at 12:00 PM\n'
                '⤇ zoom : 654 6441 0113\n'
                'Ethics147 class at 03:00 PM\n' 
                '### Reminder: klk mcq test ache\n'
                '⤇ zoom : 66849672192"\n'
        )

    @commands.command()
    async def exam(self, ctx):
        await ctx.send("EEE (1-1) @ 15/11/2020! :v:")
    
    @commands.command()
    async def assignment(self, ctx):
        await ctx.send('No assignments! Horray! :partying_face:')

def setup(client):
    client.add_cog(mComms(client))