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
                '#_10_11_20\n'
                'Project 150 workshop at 7:00 PM\n'
        )

    @commands.command()
    async def exam(self, ctx):
        await ctx.send("**EEE 1-1:**\n"
                        "Quiz\n"
                        "15 November\n"
                        "Chapter 1, 2, 3, 4, 6, 7\n"
                        " \n"
                        "**Math:**\n"
                        "Presentation + Viva\n"
                        "Starting from 20 November.\n"
                        "Presentation must be hand written. At least 20 minutes of presentation required. Differential Calculus.\n" 
                        " \n"
                        "**Ethics:**\n"
                        "Quiz\n"
                        "16 November.\n"  
                        "Everything discussed starting from plagiarism.\n")
    
    @commands.command()
    async def assignment(self, ctx):
        await ctx.send('Assignments upcoming! :partying_face:')

def setup(client):
    client.add_cog(mComms(client))