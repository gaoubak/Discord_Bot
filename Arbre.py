from connexion import *
class Node : 
    def __init__(self, question, keyword, list_node): 
        self.question = question
        self.key_word = keyword
        self.list_node = list_node
        
        

   

nodePrincipal = Node("Ceci est un node de test", "test", [Node("Tu es dans le second node de test", "deux", [Node("Tu es dans le troisieme node de test", "trois", [])])])

first_node = Node("Comment puis-je vous aidez ?","help",
[Node("Sur quel sujet ?", "cours",[Node("Sur quel cours en particulier ?", 'python', [])]), 
Node("Sur quel domaine ?", "fichier",["Sur quel fichier en particulier"])])

nodeGaming = Node("Bienvenue dans le Game'Otron. Je vais vous poser des questions et ensuite je vous indiquerai le style de jeu qui vous correspond le plus. Vous devrez répondre par 'oui' ou 'non'. Êtes vous prêt ?", "jeu",
[Node("Sur quel sujet ?", "oui",[Node("Sur quel cours en particulier ?", 'python', [])]), 
Node("Sur quel domaine ?", "non",["Bon bah rip"])])

nodeByKade = Node("Bienvenue sur le  Botkedex , est un outil de recherche sur les Pokémon. Il enregistre et apprend aux dresseurs les caractéristiques de chaque Pokémon", "pokemon", [])

''' liste choix à donner en guise de réponse '''
mycursor.execute("SELECT * FROM pokemon where name = `pikachu` ")

Aventure = 0
Arcade = 0
Combat = 0 
Sportif = 0
Musique = 0
Fete = 0
Plateformes = 0
Casse_tête = 0 
Course = 0 
Rpg = 0
Jeu_de_tir = 0 
Simulation = 0 
Sports = 0 
Stratégie = 0

actual_node = nodeByKade


