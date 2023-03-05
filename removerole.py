import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.command()
async def removeroles(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass

client.run("YOUR DISCORD BOT TOKEN HERE")
