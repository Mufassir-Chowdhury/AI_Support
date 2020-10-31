import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit = amount + 1)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: .clear {number of messages to be deleted}')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the permission to delete messages in this channel.')
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member : discord.Member, *, reason = None):
        await member.kick(reason = reason)
        await ctx.send(f'Kicked {member.mention}')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: .kick @{user name}')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the permission to kick in this channel.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.send(f'Banned {member.mention}')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: .ban @{user name}')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the permission to ban in this server.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: .unban @{user name}')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the permission to unban in this server.')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid command!')
        else:
            print('idk what to do')

def setup(client):
    client.add_cog(Moderation(client))