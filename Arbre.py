class Node : 
    def __init__(self, question, keyword, list_node):
        self.question = question
        self.key_word = keyword
        self.list_node = list_node

    def user_response(self, txt):
        print(self.question)
        txt = input()
        for Node in self.list_node:
            if Node.keyword in txt:
                Node.user_response()

first_node = Node("Comment puis-je vous aidez ?","help",
 [Node("Sur quel sujet ?", "cours",[]), Node("Sur quel domaine ?", "fichier",[])])
