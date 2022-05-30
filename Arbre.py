class Node : 
    def __init__(self, question, keyword, list_node): 
        self.question = question
        self.key_word = keyword
        self.list_node = list_node

   

nodePrincipal = Node("Ceci est un node de test", "test", [Node("Tu es dans le second node de test", "deux", [Node("Tu es dans le troisieme node de test", "trois", [])])])

first_node = Node("Comment puis-je vous aidez ?","help",
[Node("Sur quel sujet ?", "cours",[Node("Sur quel cours en particulier ?", 'python', [])]), 
Node("Sur quel domaine ?", "fichier",["Sur quel fichier en particulier"])])

actual_node = nodePrincipal


