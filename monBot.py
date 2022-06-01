from asyncio import events
import discord
from random import randint 
from discord.ext import commands
import json
from Arbre import *
from connexion import *


intents = discord.Intents.all()

# La commande commence par '!'
client = commands.Bot(command_prefix="!", intents=intents)

@client.command()
# On execute la commande '!' + nomDeLaFonction
async def coucou(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send("Coucou !")


@client.command()
async def server(ctx):
    name = ctx.guild.name
    description = ctx.guild.description
    owner = ctx.guild.owner
    id = ctx.guild.id
    region = ctx.guild.region
    member_count = ctx.guild.member_count
    icon = ctx.guild.icon_url

    embed = discord.Embed(
        title = name ,
        description = description,
        color = discord.Color.red()
    )
    embed.set_thumbnail(url = icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server Id", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=member_count, inline=True)
    
    await ctx.send(embed = embed)


        


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
    global actual_node

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
   
    if actual_node.key_word in message.content:
        await message.channel.send(actual_node.question)
        
    for Node in actual_node.list_node:
        if Node.key_word in message.content:
            await message.channel.send(Node.question)
            actual_node = Node
            
        

 

        

    if message.content.startswith('$aidemoipour'):
        content = msg.split("$aidemoipour ",1)[1]
        await message.channel.send(content)

    if message.content.startswith('$randopok'):
        ''' content = msg.split("$randopok ",1)[1] '''
        random = str(randint(1, 151))
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM pokemon where id_pok = " + random)
        myresult = mycursor.fetchall()
        for value in myresult:
            id_pok = value[0]
            nom_pok = value[1]
            type_1 = value[2]
            type_2 = value[3]
            evolue_avec = value[4]
            description_pok = value[5]
            dresseur = value[6]
            couleur = value[7]

        embed = discord.Embed(
            title = nom_pok,
            description = description_pok,
            color = discord.Color.red()
        )
        embed.add_field(name="Type 1", value=type_1, inline=True)
        embed.add_field(name="Type 2", value=type_2, inline=True)
        embed.add_field(name="Region", value=nom_pok, inline=True)
        embed.add_field(name="Member Count", value=nom_pok, inline=True)
        
        await message.channel.send(embed = embed)

    

        


    await client.process_commands(message)

client.run('OTc4MjYyOTUzMTA1MTc0NTg4.Gx1ohw.Ew_8UjtIANzy5d0xvN6DjSN-g5qL8Xh3fxNfA4')