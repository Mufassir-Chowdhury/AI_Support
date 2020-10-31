import discord
from discord import colour
from discord.ext import commands

class mComms(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command('help')
    
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

    @commands.command()
    async def help(self, ctx):
        emb = discord.Embed(
            colour = discord.Colour.orange()
        )

        emb.set_author(name = 'Help')
        emb.add_field(name=':police_officer: Moderation:', value='for moderators and admins\n', inline=False)
        emb.add_field(name=':wastebasket: Delete Messages', value='.clear numofmsg', inline=True)
        emb.add_field(name=':no_entry_sign: Ban', value='.ban mention', inline=True)
        emb.add_field(name=':passport_control: Kick', value='.kick mention', inline=True)
        emb.add_field(name=':handshake: Unban', value='.unban username#ID', inline=True)
        emb.add_field(name='.\n', value='.\n', inline=False)

        emb.add_field(name=':speech_balloon: Message Commands:', value='for everyone\n', inline=False)
        emb.add_field(name=':books: Assignements', value='.assignment', inline=True)
        emb.add_field(name=':school: Classes', value='.class', inline=True)
        emb.add_field(name=':100: Exam', value='.exam', inline=True)
        emb.add_field(name=':bell: Ping', value='.ping', inline=True)
        emb.add_field(name='.\n', value='.\n', inline=False)

        emb.add_field(name=':tools: Settings:', value='for everyone\n', inline=False)
        emb.add_field(name=':mailbox: Change prefix', value='.changeprefix', inline=True)
        emb.add_field(name=':mailbox: Current Prefix', value='.currentprefix', inline=True)

        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(mComms(client))