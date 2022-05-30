from asyncio import events
import discord
from random import randint 
from discord.ext import commands
import json
from Arbre import *

intents = discord.Intents.all()

# La commande commence par '!'
client = commands.Bot(command_prefix="!", intents=intents)

@client.command()
# On execute la commande '!' + nomDeLaFonction
async def coucou(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send("Coucou !")


# Si un membre nous rejoint
@client.event
async def on_member_join(member):
    General_channel = client.get_channel(978261134878605424)
    await General_channel.send('Bonjour ' + member.display_name + 'Je suis là pour vous aider à trouver de la documentation.')
    await General_channel.send('Appeler moi avec la commande' + '"!"' + 'votreMessage')
    

   

  

# Début de l'existence du bot
@client.event
async def on_message(message):
    message.content = message.content.lower()
    msg = message.content

    if message.author == client.user:
        return

    # Dans le channel help uniquement
    Help_channel = client.get_channel(978271654608261180)
    if message.channel == Help_channel and message.content.startswith('$help'):
        await Help_channel.send('Tu es au bonne endroit :)')
    # Fin de l'instruction

    if message.channel != Help_channel and message.content.startswith('$help'):
        if message.author.id == 332936281887604747:
            await message.channel.send('Salut boss !')
        else :
            await message.channel.send('Bonjour, je suis ton heureux serviteur !')

    # Supprimer les 3 derniers messages.
    if message.content == "del":
        await message.channel.purge(limit=3)

    
    # Dire bonjour 
    if message.content.startswith('$bonjour'):
        await message.channel.send("Bonjour " + message.author.name + " !")


    # Commencer la discussion
    if test_node.key_word in message.content:
        await message.channel.send(test_node.question)
        test_node = test_node.list_node

        

    if message.content.startswith('$aidemoipour'):
        test = msg.split("$aidemoipour ",1)[1]
        
        await message.channel.send(test)

        


    await client.process_commands(message)

client.run('OTc4MjYyOTUzMTA1MTc0NTg4.Gx1ohw.Ew_8UjtIANzy5d0xvN6DjSN-g5qL8Xh3fxNfA4')