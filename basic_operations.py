import discord
from discord.ext import commands


class basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online and active')
        # Message for admin that bot is running
        await self.client.change_presence(status=discord.Status.idle,
                                          activity=discord.Game('your mum'))

    @commands.Cog.listener()
    async def on_member_join(member):
        print(f"{member} has joined a server.")
        # Message send when member joins the server

    @commands.Cog.listener()
    async def on_member_remove(member):
        print(f"{member} has left the channel.")
        # Message send when member left the server

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        # Command for kicking

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        # command for banning

    @commands.command()
    async def unban(slef, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discrim = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name,
                                                   member_discrim):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')

                return   # command for unbaning the user

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)  # command for clearing chat


def setup(client):
    client.add_cog(basic(client))
