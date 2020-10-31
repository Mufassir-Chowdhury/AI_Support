import discord
from discord import colour
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command('help')

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
        emb.add_field(name='.\n', value='.\n', inline=False)

        emb.add_field(name=':desktop: Source Code', value='https://github.com/Mufassir-Chowdhury/AI_Support.git', inline=False)

        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Help(client))