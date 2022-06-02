from connexion import *
class Node : 
    def __init__(self, question, keyword, list_node): 
        self.question = question
        self.key_word = keyword
        self.list_node = list_node
        
        

   

nodePrincipal = Node("Besoin d'aide sur quel language de programmation ?", "programme", 
[Node("Voici une documentation sur PHP : https://www.php.net/manual/fr/", "php", []),
Node("Voici une documentation sur HTML : https://www.php.net/manual/fr/", "html", [])] 
)

first_node = Node("Dites moi tout, je suis là !","$cours",
[Node("Sur quel sujet ?", "cours",[Node("Sur quel cours en particulier ?", 'python', [])]), 
Node("Sur quel domaine ?", "fichier",["Sur quel fichier en particulier"])])


nodeByKade = Node("Bienvenue sur le  Botkedex , est un outil de recherche sur les Pokémon. Il enregistre et apprend aux dresseurs les caractéristiques de chaque Pokémon", "pokemon", [])

''' liste choix à donner en guise de réponse '''

nom_pok = ""
actual_node = nodePrincipal


