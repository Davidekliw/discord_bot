import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import logging

handler = logging.FileHandler(filename="discord.log", mode='w', encoding="utf-8")

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def hallo(ctx):
    await ctx.send(f"Grüße dich {ctx.author.mention}")

new_role = "hammerTyp"

async def haveItCheck(ctx):
    #print('I see the following roles: ' + ', '.join(ctx.author.roles))
    for role in ctx.author.roles:
        result = role.find(ctx)
        return result


async def roles(ctx, newrole):
    haveIt = False
    for role in ctx.author.roles:
        if role.name == new_role:
            haveIt = True

    if haveIt:
        #print(f"Du hast diese Rolle bereits: {new_role}")
        await ctx.send(f"Du hast diese Rolle bereits")
        return
    else:
        await ctx.author.add_roles(newrole)
        await ctx.send(f"Deine Rolle wurde hinzugefügt")
        return
    

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    if role:
        await roles(ctx, role)
        return
    await ctx.send(f"Die Rolle {role} wurde nicht gefunden.")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"Deine Rolle wurde hinzugefügt")
        return
    await ctx.send(f"Die Rolle {role} wurde nicht gefunden.")

@bot.command()
async def msg(ctx, arg):
    await ctx.send(f"deine Nachricht war {arg}")

@bot.event
async def on_ready():
    print(f"Ready! Und ich bin {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "banana" in message.content.lower():
        await message.delete()
        channel = message.channel
        await channel.send(f" Hallo das darf nicht jeder sagen: {message.author}!")

    await bot.process_commands(message)


bot.run(token, log_handler=handler, log_level=logging.DEBUG)

if __name__ == "__main__":
    #print(token)
    pass