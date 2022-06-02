from platform import node
from connexion import *
class Node : 
    def __init__(self, question, keyword, list_node): 
        self.question = question
        self.key_word = keyword
        self.list_node = list_node

    
# Voici des Nodes que le bot utilise afin de cerner les besoins de l'utilisateur.
nodePythonExo = Node("Si vous voulez des exercices de Python, je peux vous en fournir sans problème : https://info.blaisepascal.fr/exercices-python", "exercice", [])
nodePHPExo = Node("Si vous voulez des exercices de PHP, je peux vous en fournir sans problème : https://aymeric-auberton.fr/academie/php/exercices", "exercice", [])
nodeHTMLExo =Node("Si vous voulez des exercices de HTML, je peux vous en fournir sans problème : https://aymeric-auberton.fr/academie/html/exercices/", "exercice", [])
nodeCssExo = Node("Si vous voulez des exercices de CSS, je peux vous en fournir sans problème : https://aymeric-auberton.fr/academie/css/exercices/", "exercice", [])

nodePython = Node("Voici le saint manuel du Python : https://docs.python.org/fr/3/tutorial/ Avez vous besoin d'exercice en plus ?", "python", [nodePythonExo])
nodePHP = Node("Voici le saint manuel du PHP : https://www.php.net/manual/fr/ Avez vous besoin d'exercice en plus ?", "php", [nodePHPExo])
nodeHtml = Node("Voici le saint manuel du HTML : https://developer.mozilla.org/fr/docs/Learn/HTML Avec vous besoin d'exercice en plus ?", "html", [nodeHTMLExo])
nodeCss = Node("Voici le saint manuel du CSS : https://developer.mozilla.org/fr/docs/Web/CSS Avez vous besoin d'exercice en plus ?", "css", [nodeCssExo])

nodeProgrammation = []
nodePrincipal = Node("Je suis là !", "help", [Node("Merci de me préciser quel langage de programmation", "programmation", [nodePython, nodeCss, nodeHtml, nodePHP])])





nodeByKade = Node("Bienvenue sur le  Botkedex , est un outil de recherche sur les Pokémon. Il enregistre et apprend aux dresseurs les caractéristiques de chaque Pokémon", "pokemon", [])

# Variables globales qui nous sont utile dans monBot.py 
nom_pok = ""
memory_node = nodePrincipal
actual_node = nodePrincipal


