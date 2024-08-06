import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command()
async def apelar(ctx, *, appeal: str):
    review_channel = bot.get_channel(int(os.getenv('CHANNEL_ID')))
    await review_channel.send(f'Apelación de {ctx.author}:\n{appeal}')
    await ctx.author.send('Tu apelación ha sido enviada y será revisada pronto.')

@bot.command()
@commands.has_permissions(administrator=True)
async def aprobar(ctx, user: discord.User):
    guild = ctx.guild
    await guild.unban(user)
    await ctx.send(f'{user.mention} ha sido desbaneado.')

bot.run(os.getenv('MTI3MDM2MTQ3NjY3NDM1OTQxOA.Gpb29e.s6dfL03UuYmQjXxDv3ErK3waepJOafZRzwfRew'))
