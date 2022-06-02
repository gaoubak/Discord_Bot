from asyncio import events
from importlib.metadata import files
import discord
from random import randint 
from discord.ext import commands
import json
from Arbre import *
from connexion import *


intents = discord.Intents.all()

# La commande commence par '!'
client = commands.Bot(command_prefix="!", intents=intents)

#@client.command()
# On execute la commande '!' + nomDeLaFonction
#async def coucou(ctx):
#    await ctx.channel.purge(limit=1)
#    await ctx.send("Coucou !")

      


# Si un membre nous rejoint, envoi un message de salutation.
@client.event
async def on_member_join(member):
    General_channel = client.get_channel(978261134878605424)
    await General_channel.send('Bonjour ' + member.display_name + 'Taper "$help" pour connaitre mes fonctionnalités.')
 


# Début de l'existence du bot
@client.event
async def on_message(message):
    message.content = message.content.lower()
    msg = message.content
    global actual_node
    global nom_pok

    if message.author == client.user:
        return

    # Dans le channel help uniquement
    #Help_channel = client.get_channel(978271654608261180)
    #if message.channel == Help_channel and message.content.startswith('$cmd'):
        #await Help_channel.send('Tu es au bonne endroit :)')
    # Fin de l'instruction

    #if message.channel != Help_channel and message.content.startswith('$cmd'):
        #if message.author.id == 332936281887604747:
            #await message.channel.send('Salut boss !')
        #else :
            #await message.channel.send('Bonjour, je suis ton heureux serviteur !')

    # Supprimer les X derniers messages seulement si le membre est administrateur.
    if message.content.startswith('$del'):
        if message.author.guild_permissions.administrator:
            content = int(msg.split("$del ",1)[1])
            await message.channel.purge(limit=content)
        else:
            await message.channel.send("Vous n'êtes pas autorisé à faire ça.")

   
    
    # Dire bonjour 
    if message.content.startswith('$bonjour'):
        await message.channel.send("Bonjour " + message.author.name + " !")

    # Commencer la discussion
   
    #if actual_node.key_word in message.content:
     #   await message.channel.send(actual_node.question)
        
    #for Node in actual_node.list_node:
     #   if Node.key_word in message.content:
      #      await message.channel.send(Node.question)
       #     actual_node = Node
            
            
        
    if message.content.startswith('$moderateur'):
        member = message.author
        channel = client.get_channel(978261134878605424)
        await channel.send(f"{member.mention} a besoin d'aide !\n<@&981837677588520960>")

    # afficher les commande
    if message.content.startswith('$help'):
        cmd_1 = "Le bot aléatoirement un pokemon de la première génération."
        cmd_2 = "Vous permet d'entrer une réponse."
        cmd_6 = "Relance le jeu et choisi un nouveau pokémon"
        cmd_3 = "Supprime les X derniers messages dans le channel."
        cmd_4 = "Le bot vous dit bonjour."
        cmd_5 = "Permet d'appeler un modérateur."
        cmd_7 = "Permet d'obtenir un lien vers la page d'un pokémon."
        embed2 = discord.Embed(
                title = "Commande of the Ri bot",
                description = "Vous trouverez ici un resumé de chaque commande du bot",
                color = discord.Color.green()
            )
        embed2.add_field(name="$randopok", value=cmd_1, inline=True)
        embed2.add_field(name="$r", value=cmd_2, inline=True)
        embed2.add_field(name="$randopokreset", value=cmd_6, inline=True)
        embed2.add_field(name="$del X", value=cmd_3, inline=True)
        embed2.add_field(name="$bonjour", value=cmd_4, inline=True)
        embed2.add_field(name="$moderateur", value=cmd_5, inline=True)
        embed2.add_field(name="$pokedex", value=cmd_7, inline=True)

        
        await message.channel.send(embed = embed2)


    # Choisi un pokémon aléatoirement
    if message.content.startswith('$randopok'):
<<<<<<< HEAD
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
        embed.add_field(name="evolution", value=evolue_avec, inline=True)
        embed.add_field(name="Member Count", value=nom_pok, inline=True)
=======
        if(nom_pok == "") or message.content.startswith('$randopokreset'):
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
            
>>>>>>> 689b744140c9c19d19a3f1a88a68bad6346fd893
        
            embed = discord.Embed(
                title = "Pokemon mystère !",
                description = description_pok,
                color = discord.Color.red()
            )

            embed.add_field(name="Type1", value=type_1, inline=True)

            if(type_2 != ""):
                embed.add_field(name="Type2", value=type_2, inline=True)

            if(evolue_avec != ""):
                embed.add_field(name="Indice évolution", value=evolue_avec, inline=True)
            
            
            await message.channel.send(embed = embed)
        else:
            await message.channel.send("Vous n'avez pas trouvé le pokémon précédent... :(")
            await message.channel.send("Vous pouvez relancer le jeu en taper $randopokreset.")


    # Pour envoyer ça réponse, on tape '$r nomDuPokemon'
    if message.content.startswith('$r'):
        content = msg.split("$r ",1)[1]
        if(content == nom_pok.lower()):
            await message.channel.send('Bravo tu as trouvé la réponse')
            await message.channel.send(file=discord.File('./1G/'+ nom_pok + '.gif'))
            nom_pok = ""
        else:
            await message.channel.send('Echec...')
            

    # Recjerche un pokémon pour l'utilisateur et lui renvoie un lien
    if message.content.startswith('$pokedex'):
        content = msg.split("$pokedex ",1)[1]

        if(content.lower() == 'nidoranm' or content.lower() == 'nidoranf'):
           if(content.lower() == 'nidoranm'):
               await message.channel.send('https://www.pokemon.com/fr/pokedex/nidoran-male/')
               return
           else:
               await message.channel.send('https://www.pokemon.com/fr/pokedex/nidoran-female/')
               return
        
        await message.channel.send('https://www.pokemon.com/fr/pokedex/'+content+'/')
    

        


    await client.process_commands(message)

client.run('OTc4MjYyOTUzMTA1MTc0NTg4.Gx1ohw.Ew_8UjtIANzy5d0xvN6DjSN-g5qL8Xh3fxNfA4')