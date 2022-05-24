import discord
from random import randint 
from discord.ext import commands
intents = discord.Intents.all()

# La commande commence par '!'
client = commands.Bot(command_prefix="!", intents=intents)

@client.command()
# On execute la commande '!' + nomDeLaFonction
async def coucou(ctx):
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

    if message.author == client.user:
        return

    # Dans le channel help uniquement
    Help_channel = client.get_channel(978271654608261180)
    if message.channel == Help_channel and message.content.startswith('$help'):
        await Help_channel.send('Tu es au bonne endroit :)')
    # Fin de l'instruction


    if message.channel != Help_channel and message.content.startswith('$help'):
        if message.author.name == "ri":
            await message.channel.send('Salut boss !')
            ''' await message.channel.send(message.author.id) '''
        else :
            await message.channel.send('Bonjour, je suis ton heureux serviteur !')

    if message.content == "del":
        await message.channel.purge(limit=3)
    await client.process_commands(message)

client.run('OTc4MjYyOTUzMTA1MTc0NTg4.Gx1ohw.Ew_8UjtIANzy5d0xvN6DjSN-g5qL8Xh3fxNfA4')