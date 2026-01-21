import discord
from discord.ext import commands
import random
import os
import requests


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

@bot.command()
async def hello (ctx):
    await ctx.send(f"Hi! I am a bot {bot.user}!")

@bot.command()
async def help (ctx):
    await cttx.send (f"PANDUAN BOT \n ?tantangan = untuk challange harian \n ?fakta = untuk fakta terkini tentang sampah \n UNTUK ?recycle menggunakan panduan tertentu \n ?recycle_p = untuk mencari cara recylce sampah plastik \n ?recycle_so = untuk mencari cara recylce sampah organik/limbah rumah tangga ")

@bot.command()
async def tantangan(ctx):
    challengerandom=[
        "Gunakanlah sedotan reuseable seharian penuh!",
        "Buatlah sesuatu dari sampah yang kamu buang hari ini!",
        "Khusus hari ini challenge Plastic Bag Refusal Day ",
        "Edukasi orang-orang terdekatmu tentang sampah!"
    ]
    await ctx.send(f"TANTANGAN HARI INI ADALAH\n{random.choice(challengerandom)}")

@bot.command()
async def fakta(ctx):
    faktarandom=[
        "Setiap tahun, dunia menghasilkan 2,12 miliar to sampah",
        "Indonesi peringkat #4 penghasil sampah plastik laut terbesar di dunia",
        "1,1 juta botol plastik dibeli setiap menit di seluruh dunia",
        "Hanya 9% plastik yang pernah di daur ulang",
        "Di Indonesia hanya 60% sampah terkelola dengan baik"
    ]
    await ctx.send(f"FAKTA TERKINI\n{random.choice(faktarandom)}")

@bot.command()
async def recycle(ctx):
    await ctx.send("gunakan perintah ?recyle(nama sampah berupa singkatan, ketik ?help untuk meminta bantuan!)")


bot.run(token)
