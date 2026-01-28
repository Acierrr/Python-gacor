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

bot = commands.Bot(command_prefix='?', description=description, intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

@bot.command()
async def hello (ctx):
    await ctx.send(f"Hi! I am a bot {bot.user}!")

@bot.command()
async def help(ctx):
    help_text = f"""
PANDUAN BOT
• ?tantangan = untuk challenge harian
• ?fakta = untuk fakta terkini tentang sampah
• ?recycle [material] = untuk informasi daur ulang (gunakan: plastik, kardus, kaca, dll)
• ?hello = untuk menyapa bot
"""
    await ctx.send(help_text)

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
async def recycle(ctx,material):
    if material is None:
        await ctx.send(f"Cara menggunakan:?recycle [nama_material]\nContoh: ?recycle plastik atau ?recycle kardus")
        return
    
    material = material.lower()  

    recycle_info = {
        "plastik": """
    DAUR ULANG PLASTIK:
    1. Bersihkan dari sisa makanan/minuman
    2. Lepaskan label dan tutup (jika berbeda jenis)
    3. Keringkan sebelum disimpan
    4. Pisahkan berdasarkan kode resin (angka dalam segitiga)
    5. Bawa ke bank sampah atau dropbox daur ulang
    """,
        
        "kardus": """
    DAUR ULANG KARDUS:
    1. Ratakan kardus untuk menghemat space
    2. Lepaskan selotip, staples, dan plastik pembungkus
    3. Pastikan kardus tidak basah atau berminyak
    4. Kumpulkan dan bawa ke pengepul atau bank sampah
    """,
        
        "kaca": """
    DAUR ULANG KACA:
    1. Cuci bersih dari sisa makanan/minuman
    2. Pisahkan berdasarkan warna (jernih, hijau, cokelat)
    3. Hati-hati dengan pecahan kaca
    4. Jangan campur dengan keramik atau piring kaca
    """,
        
        "kaleng": """
    DAUR ULANG KALENG:
    1. Cuci bersih dari sisa makanan/minuman
    2. Keringkan sebelum disimpan
    3. Ratakan atau tekan untuk menghemat ruang
    4. Pisahkan kaleng aluminium dan baja
    5. Bawa ke pusat daur ulang atau bank sampah
    """
    }

    if material in recycle_info:
        await ctx.send(recycle_info[material])
    else:
        await ctx.send(f"Material '{material}' tidak ditemukan.")



bot.run('TOKEN')
