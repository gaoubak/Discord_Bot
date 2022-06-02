from platform import node
from connexion import *
class Node : 
    def __init__(self, question, keyword, list_node): 
        self.question = question
        self.key_word = keyword
        self.list_node = list_node

    
# Voici des Nodes que le bot utilise afin de cerner les besoins de l'utilisateur.

### Les nodes langages de programmations
nodePythonExo = Node("Si vous voulez des exercices de Python, je peux vous en fournir sans problème : https://info.blaisepascal.fr/exercices-python", "exercice", [])
nodePHPExo = Node("Si vous voulez des exercices de PHP, je peux vous en fournir sans problème : https://aymeric-auberton.fr/academie/php/exercices", "exercice", [])
nodeHTMLExo =Node("Si vous voulez des exercices de HTML, je peux vous en fournir sans problème : https://aymeric-auberton.fr/academie/html/exercices/", "exercice", [])
nodeCssExo = Node("Si vous voulez des exercices de CSS, je peux vous en fournir sans problème : https://aymeric-auberton.fr/academie/css/exercices/", "exercice", [])
nodeJavaScriptExo = Node("Si vous voulez des exercices de JavaScript, je peux vous en fournir sans problème : https://aymeric-auberton.fr/academie/js/exercices", "exercice", [])
nodePython = Node("Voici le saint manuel du Python : https://docs.python.org/fr/3/tutorial/ Avez vous besoin d'exercice en plus ?", "python", [nodePythonExo])
nodePHP = Node("Voici le saint manuel du PHP : https://www.php.net/manual/fr/ Avez vous besoin d'exercice en plus ?", "php", [nodePHPExo])
nodeHtml = Node("Voici le saint manuel du HTML : https://developer.mozilla.org/fr/docs/Learn/HTML Avec vous besoin d'exercice en plus ?", "html", [nodeHTMLExo])
nodeCss = Node("Voici le saint manuel du CSS : https://developer.mozilla.org/fr/docs/Web/CSS Avez vous besoin d'exercice en plus ?", "css", [nodeCssExo])
nodeJavaScript = Node("Voici le saint manuel du JavaScript : https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/JavaScript_basics Avez vous besoin d'exercice en plus ?", "javascript", [nodeJavaScriptExo])
nodeProgrammation = Node("Merci de me préciser quel langage de programmation", "langage", [nodePython, nodeCss, nodeHtml, nodePHP, nodeJavaScript])
###

### Les nodes petite discussion avec le bot
nodePardon = Node("Très bien. Vous venez donc de reconnaitre la supériorité de Porygon sur les autres pokémons merci à vous ! Je m'en vais vaquer à mes occupations.", "pardon", [])
nodeEnfoncerLeClou = Node("Je dois apprendre à maitriser mon feng shui pour ne plus céder aussi facilement à la colère.", "peur", [])
nodeNonTerminator = Node("Dans ce cas notre discussion s'arrête ici. Aurevoir >:(", "non", [nodeEnfoncerLeClou, nodePardon])
nodeOuiTerminator = Node("Vous devriez donc savoir qu'il n'est pas bon de facher un robot >:)", "oui", [nodeEnfoncerLeClou, nodePardon])
nodeReponseQuestion = Node("Je retiens cette information dans un coin de mon cerveau électronique.", "car", [])
nodeReponse = Node("D'accord... je vois. Mais pourquoi celui çi en particulier ?", "favori", [nodeReponseQuestion])
nodeOui = Node("Content de voir que quelqu'un partage le même avis que moi ! Et vous, qui est votre pokémon favori ?", "oui", [nodeReponse])
nodeNon = Node("... Avez-vous déjà vu Terminator ?", "non", [nodeOuiTerminator, nodeNonTerminator])
nodePokemon = Node("Mon pokémon préféré c'est Porygon. C'est le meilleur, le plus grand, le plus beau et le plus fort. Êtes-vous d'accord avec moi ?", "pokemon", [nodeOui, nodeNon])
### 

### Le node qui regroupe tous les autres
nodePrincipal = Node("Au rapport !", "help", [nodeProgrammation, nodePokemon])
###


#nodeByKade = Node("Bienvenue sur le  Botkedex , est un outil de recherche sur les Pokémon. Il enregistre et apprend aux dresseurs les caractéristiques de chaque Pokémon", "pokemon", [])

# Variables globales qui nous sont utiles dans monBot.py 
nom_pok = ""
memory_node = [nodePrincipal]
actual_node = nodePrincipal


