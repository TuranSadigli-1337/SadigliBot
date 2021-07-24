#!/usr/bin/env python
# -*BSD 3-Clause License*-

#__müəllif__      = "Turan Sadigli"
#__müəllif huquqları__   = "Müəllif Hüquqları 2021, SadigliBot"
#__lizensiya__     = "BSD 3-Clause License"

import os
import json
import discord
import random
import asyncio

from random import *
from os.path import join, dirname
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import commands

# load .env file
dir_path = os.path.dirname(os.path.realpath(__file__))

dotenv_path = join(dir_path, '.env')
load_dotenv(dotenv_path)

DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

JSON_FILE = str(os.path.dirname(os.path.realpath(__file__))) + '/data.json'


def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

        return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix = get_prefix)

@bot.event
async def on_ready():
    """ BOT sunucuya bağlandı """

    print(f'{bot.user.name} sunucuya bağlandı')

    # check if bot has connected to guilds
    if len(bot.guilds) > 0:
        print('kodlar yazıldı:')

        for guild in bot.guilds:
            print(f'* {guild.name}#{guild.id}')


@bot.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

        prefixes[str(guild.id)] = "."

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

            prefixes.pop(str(guild.id))

            with open("prefixes.json", "w") as f:
                json.dump(prefixes, f, indent=4)

@bot.command()
async def prefixdəyiş(ctx, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

    await ctx.send(f"Prefix {prefix} olaraq dəyişdirildi.")


@bot.command(name="salam")
async def Salam(ctx):
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content

    await channel.send("Əleyküm")
    
@bot.command(name="necəsiz")
async def HalXetir(ctx):
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content

    await channel.send("Şükür Allaha. Botuq da. Yola veririk. Sən necəsən?")


@bot.command(name="sikayet")
async def sikayet(ctx, *, member):
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content

    await channel.send("Şikayət başarıyla göndərildi.")


@bot.command(name="şikayət")
async def shikayet(ctx):
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content

    await channel.send("Ala yenə noldu?\n\n Şikayət üçün **.sikayet @istifadəçiadı** yaz.")


@bot.command(name="adminlər")
async def adminler(ctx):
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content

    await channel.send(" ")


def yoxlama(ctx):
    return ctx.author.id == 483209522064916480


@bot.command()
@commands.check(yoxlama)
async def sil(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@bot.command()
@commands.check(yoxlama)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} kickləndi.')

@bot.command()
@commands.check(yoxlama)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} banlandı.')

@bot.command()
@commands.check(yoxlama)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):

            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} istifadəçisinin banı qaldırıldı.')
            return


if __name__ == "__main__":
    # botu başlat
    bot.run(DISCORD_TOKEN)
    
