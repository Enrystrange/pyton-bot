import discord
from discord.ext import commands
from botlogic import gen_pass,flip_coin,gen_emodji,num
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print("fHai fatto l\\'accesso come {bot.user}")

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')
@bot.command()
async def hide(ctx):
    await ctx.send(f'ㅤ')
@bot.command()
async def cerchio(ctx):
    await ctx.send(f'◌')
@bot.command()
async def ciambella(ctx):
    await ctx.send(f'◎')
@bot.command()
async def Ankh(ctx):
    await ctx.send(f'☥')
@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))
@bot.command()
async def flip(ctx):
    await ctx.send(flip_coin())
@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emodji())
@bot.command()
async def randomnum(ctx):
    await ctx.send(num())
bot.run("MTE2MDUxODYzMzk5MTE4ODUzMw.Gj204T.VSikS0k0SUj6bVWLFaICxPPXjjmP6JhREfVwdo")
