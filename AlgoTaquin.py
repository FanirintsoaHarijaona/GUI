from collections import deque
import json
import random
import numpy as np
import copy

graph = [
    [0,1,1,0,0,1,0],
    [0,0,0,0,0,0,0],
    [0,1,0,1,0,0,1],
    [0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]

class Taquin:
    """
        méthode d'initialisation du noeud de départ avant shuffle
    """
    def __init__(self):
        self.node = [[1,2,3],[4,5,6],[7,8,0]]


    """
        méthode qui retourne la valeur du noeud actuel du taquin
    """
    def get_node(self):
        return self.node

    
    """
        méthode qui permet de changer la valeur du noeud 
    """
    def set_node(self,valeur):
# créer une autre instance au lieu d'assigner la référence de l'itérable
        node = copy.deepcopy(valeur)
        self.node = node


    """
        Définition des mouvements possibles
    """
    def possible_moves(self):
        row,col = self.get_position_zero()
        position_zero = str(row)+str(col)
        #print(position_zero)
        if position_zero == "00":   return ["RIGHT","DOWN"]
        elif position_zero == "01": return ["LEFT","RIGHT","DOWN"]
        elif position_zero == "02": return ["LEFT","DOWN"]
        elif position_zero == "10": return ["RIGHT","UP","DOWN"]
        elif position_zero == "11": return ["LEFT","RIGHT","UP","DOWN"]
        elif position_zero == "12": return ["LEFT","UP","DOWN"]
        elif position_zero == "20": return ["RIGHT","UP"]
        elif position_zero == "21": return ["LEFT","RIGHT","UP"]
        elif position_zero == "22" : return ["LEFT","UP"]
        else : return "direction impossible"


    """
        méthode qui renvoie la place vide sur le noeud 
    """
    def get_position_zero(self):
        for row in range(3):
            for col in range(3):
                if self.node[row][col] == 0:
                    return row,col


    """
        méthode qui permet le déplacement
    """
    def move(self,direction):
        row,col = self.get_position_zero()
        tmp = 0
        if direction == "UP":
            tmp = self.node[row-1][col]
            self.node[row-1][col] = self.node[row][col]
            self.node[row][col] = tmp
        elif direction == "DOWN":
            tmp = self.node[row+1][col]
            self.node[row+1][col] = self.node[row][col]
            self.node[row][col] = tmp
        elif direction == "LEFT":
            tmp = self.node[row][col-1]
            self.node[row][col-1] = self.node[row][col]
            self.node[row][col] = tmp
        elif direction == "RIGHT":
            tmp = self.node[row][col+1]
            self.node[row][col+1] = self.node[row][col]
            self.node[row][col] = tmp

    def moveUp(self):
        row,col = self.get_position_zero()
        if row > 0:
            tmp = self.node[row-1][col]
            self.node[row-1][col] = self.node[row][col]
            self.node[row][col] = tmp

    def moveDown(self):
        row,col = self.get_position_zero()
        if row < 2:
            tmp = self.node[row+1][col]
            self.node[row+1][col] = self.node[row][col]
            self.node[row][col] = tmp
    def moveLeft(self):
        row,col = self.get_position_zero()
        if col > 0:
            tmp = self.node[row][col-1]
            self.node[row][col-1] = self.node[row][col]
            self.node[row][col] = tmp
    def moveRight(self):
        row,col = self.get_position_zero()
        if col < 2:
            tmp = self.node[row][col+1]
            self.node[row][col+1] = self.node[row][col]
            self.node[row][col] = tmp

    def __str__(self):
        string = ""
        for row in range(3):
            for col in range(3):
                string += str(self.node[row][col])+"|"
            string += "\n_ _ _\n"
        return string


    """
        désordonné les chiffres du taquin
    """
    def shuffle(self,n=1):
        n *= 20
        for i in range(n):
            directions = self.possible_moves()
            direc = random.choice(directions)
            self.move(direc)


"""
    Convertir le noeud en chaîne de caractères
"""
def node_to_str(node):
        #print(node)
        dictionnaire = {}
        dictionnaire["00"] = node[0][0]
        dictionnaire["01"] = node[0][1]
        dictionnaire["02"] = node[0][2]
        dictionnaire["10"] = node[1][0]
        dictionnaire["11"] = node[1][1]
        dictionnaire["12"] = node[1][2]
        dictionnaire["20"] = node[2][0]
        dictionnaire["21"] = node[2][1]
        dictionnaire["22"] = node[2][2]
        return json.dumps(dictionnaire)


"""
    fonction de transformation de la représentation en chaîne de caractères en matrice
"""
def s_to_node(string):
        dicto = json.loads(string)
        node = np.zeros((3,3))
        node[0][0] = dicto["00"]
        node[0][1] = dicto["01"]
        node[0][2] = dicto["02"] 
        node[1][0] = dicto["10"]
        node[1][1] = dicto["11"]
        node[1][2] = dicto["12"]
        node[2][0] = dicto["20"]
        node[2][1] = dicto["21"]
        node[2][2] = dicto["22"]
        return node



"""
    Fonction qui liste le voisin de chaque noeud du jeu Taquin
"""
def list_neighbours(taquin_T):
    node_init = taquin_T.get_node()
    direction = taquin_T.possible_moves()
    neighbours = []
    for i in direction:
        taq = Taquin()
        taq.set_node(node_init)
        taq.move(i)
        neighbours.append(taq.get_node())
    return neighbours



"""
    Fonction de construction de la graphe (ici on va utiliser une liste d'adjacence)
"""
def construct_graph(taquin_Init):
# variable pour stocker le graphe une fois construite
    graph = {}
# noeud final 
    taq_result = Taquin()
    node_result = taq_result.get_node()
# liste des noeuds présent dans le graphe
    node_list = []
    node_init = taquin_Init.get_node()
    node_list.append(node_init)
# enregistrement des noeuds déja traversé (après liste de ses voisins)
    node_neighbour = []
    node_neighbour.append(node_init)
    voisins = list_neighbours(taquin_Init)
# ajout des voisins du noeud après shuffle initial
    for voisin in voisins:
        node_list.append(voisin)
    graph[node_to_str(node_init)] = voisins
    while node_result not in node_list:
# effacer le noeud traversé
        del node_list[0]
# régler le noeud du taquin sur le prochain voisin dans liste
        taquin_Init.set_node(node_list[0])
        voisins_redundants = list_neighbours(taquin_Init)
# ajout dans la liste de noeuds déja traversés
        node_neighbour.append(node_list[0])
# effacer les rédondances des voisins qui sont présents dans node_list et node_neighbour
        voisins = []
        for voisin in voisins_redundants:
            if voisin not in node_list and voisin not in node_neighbour:
                voisins.append(voisin)
                node_list.append(voisin)
#construction de la liste d'adjacence
        graph[node_to_str(node_list[0])] = voisins
# traiter les noeuds restants
    while len(node_list) > 0:
        if len(node_list) == 1:
            graph[node_to_str(node_list[0])] = []
            break
        taquin_Init.set_node(node_list[0])
        voisins_redundants = list_neighbours(taquin_Init)
        node_neighbour.append(node_list[0])
        voisins = []
        for voisin in voisins_redundants:
            if voisin in node_list and voisin not in node_neighbour:
                voisins.append(voisin)
        graph[node_to_str(node_list[0])] = voisins
        del(node_list[0])
    return graph
    
"""
    Fonction qui permet les voisins pour une liste d'adjacence
"""   
def listNeighbours(graph,node):
    return graph[node_to_str(node)]

"""
    fonction de parcours en largeur de la graphe
"""
# pour liste d'adjacence
# exemple de graphe : {1:[2,3],2:[4,3]}
def bfs_taquin(graph,taquin_t):
    liste_predecesseur = {}
    stock = deque()
    colored = []
    node = taquin_t.get_node()
    stock.append(node)
    liste_predecesseur[node_to_str(node)] = node
    voisins = listNeighbours(graph,node)
    for voisin in voisins:
        if voisin not in colored:
            liste_predecesseur[node_to_str(voisin)] = node
            stock.append(voisin)
    colored.append(node)
    stock.popleft()
    while len(stock) > 0 :
        node = stock[0]
        voisins = listNeighbours(graph,node)
        for voisin in voisins:
            if voisin not in colored:
                liste_predecesseur[node_to_str(voisin)] = node
                stock.append(voisin)
        colored.append(node)
        stock.popleft()
    return liste_predecesseur

"""
    Fonction de résolution du jeu 
"""
def resolve(liste_bfs,sommet_initial):
    node_res = [[1,2,3],
            [4,5,6],
            [7,8,0]]
    resolv = []
    resolv.append(node_res)
    resolv.append(liste_bfs[node_to_str(node_res)])
    while(resolv[-1]!=sommet_initial):
        resolv.append(liste_bfs[node_to_str(resolv[-1])])
    return resolv


def represent_solution(tabSolve):
    t = Taquin()
    longueur = len(tabSolve)
    for i in range(longueur):
        t.set_node(tabSolve[longueur-i-1])
        print(t)
        print("\n")


     

if __name__=="__main__":
    #print(bfs(graph,0))
    t = Taquin()
    t.shuffle(2)
    print("Sommet initial")
    #sommet_initial = t.get_node()
    #t.set_node([[0, 1, 3], [4, 2, 6], [7, 5, 8]])
    sommet_initial = t.get_node()
    print(sommet_initial)
    print("Construction graphe")
    graph = construct_graph(t)
    #print(graph)
    print("\tEffectué")
# récupérer la valeur de départ du noeud de Taquin
    t.set_node(sommet_initial)
    print("parcours en largeur de la graphe")
    
    liste_bfs = bfs_taquin(graph,t)
    print("\tEffectué")
    print("Résolution du jeu")
    represent_solution(resolve(liste_bfs,sommet_initial))
    print("\tRésolu")
    

    
    