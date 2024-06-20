import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def zar_at(ctx):
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)
    await ctx.send(f'Zarlar: {zar1} ve {zar2}. Toplam: {zar1 + zar2}')

@bot.command()
async def tkm(ctx, secim: str):
    secenekler = ['taş', 'kağıt', 'makas']
    bot_secimi = random.choice(secenekler)

    if secim.lower() not in secenekler:
        await ctx.send('Geçersiz seçim! Lütfen "taş", "kağıt" veya "makas" seçin.')
        return

    if secim.lower() == bot_secimi:
        await ctx.send(f'Ben de {bot_secimi} seçtim. Berabere!')
    elif (secim.lower() == 'taş' and bot_secimi == 'makas') or \
         (secim.lower() == 'kağıt' and bot_secimi == 'taş') or \
         (secim.lower() == 'makas' and bot_secimi == 'kağıt'):
        await ctx.send(f'Ben {bot_secimi} seçtim. Kazandınız!')
    else:
        await ctx.send(f'Ben {bot_secimi} seçtim. Kaybettiniz!')

bot.run("")  #<------------- TOKENİNİ BURAYA GİR
