import discord
from discord.ext import commands
import random

import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='?', description='bot', intents=intents)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- inicio ^
@bot.command()
async def rec(ctx):
    content = random.randint(1, 4)
    if content == 1:
        resultado = '**Garrafa Pet**' \
        '\n Pode ser transformada em várias coisas, como vasos, brinquedos e muito mais.' \
        '\n Como transformar em um vaso:' \
        '\n **Materiais:**' \
        '\n - Garrafa Pet' \
        '\n - Tesoura' \
        '\n - Tinta ou caneta' \
        '\n' \
        '\n **Passo a passo:**' \
        '\n **1**. Limpe a garrafa e retire qualquer sujeira.' \
        '\n **2**. Corte a garrafa conforme necessário.' \
        '\n **3**. Forme a garrafa como quiser.' \
        '\n **4**. Decore o vaso como quiser.'
        await ctx.send(resultado)
    elif content == 2:
        resultado = '**Papel**' \
        '\n Pode ser transformado em várias coisas, como caixas, livros, papel de parede e muito mais.' \
        '\n Como transformar em uma caixa:' \
        '\n' \
        '\n **Materiais:**' \
        '\n - Papel de lixo ou papelão' \
        '\n - Tesoura' \
        '\n - Lápis ou caneta' \
        '\n' \
        '\n **Passo a passo:**' \
        '\n **1**. Corte o papel em forma de caixa.' \
        '\n **2**. Dobre os lados para criar as paredes da caixa.' \
        '\n **3**. Cole as bordas com fita adesiva ou cola.' \
        '\n **4**. Decore a caixa como quiser.'
        await ctx.send(resultado)
    elif content == 3:
        resultado = '**Metal**' \
        '\n Pode ser transformado em várias coisas, como ferramentas, móveis e muito mais.' \
        '\n Como transformar em uma ferramenta:' \
        '\n' \
        '\n **Materiais:**' \
        '\n - Latão ou ferro' \
        '\n - Martelo' \
        '\n - Serra' \
        '\n' \
        '\n **Passo a passo:**' \
        '\n **1**. Limpe o metal e retire qualquer sujeira.' \
        '\n **2**. Corte o metal conforme necessário.' \
        '\n **3**. Forme o metal como quiser.' \
        '\n **4**. Decore a ferramenta como quiser.'
        await ctx.send(resultado)
    elif content == 4:
        resultado = '**Vidro**' \
        '\n Pode ser transformado em várias coisas, como recipientes, janelas e muito mais.' \
        '\n Como transformar em um recipiente:' \
        '\n' \
        '\n **Materiais:**' \
        '\n - Vidro quebrado' \
        '\n - Tesoura' \
        '\n - Lápis ou caneta' \
        '\n' \
        '\n **Passo a passo:**' \
        '\n **1**. Limpe o vidro e retire qualquer sujeira.' \
        '\n **2**. Corte o vidro conforme necessário.' \
        '\n **3**. Forme o vidro como quiser.' \
        '\n **4**. Decore o recipiente como quiser.'
        await ctx.send(resultado)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Commando
^

bot.run('***')
