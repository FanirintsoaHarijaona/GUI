import PySimpleGUI as sg
import time
from AlgoTaquin import *

layout = [
    [sg.Button(image_filename = "assets/numero-1.png",key="BUTTON-1",border_width=0),
    sg.Button(image_filename = "assets/numero-2.png",key="BUTTON-2", border_width=0),
    sg.Button(image_filename = "assets/numero-3.png",key="BUTTON-3", border_width=0),
    ],
    [sg.Button(image_filename = "assets/numero-4.png",key="BUTTON-4", border_width=0),
    sg.Button(image_filename = "assets/numero-5.png",key="BUTTON-5", border_width=0),
    sg.Button(image_filename = "assets/numero-6.png",key="BUTTON-6", border_width=0),
    ],
    [sg.Button(image_filename = "assets/numero-7.png",key="BUTTON-7", border_width=0),
    sg.Button(image_filename = "assets/numero-8.png",key="BUTTON-8", border_width=0),
    sg.Button(image_filename = "assets/numero-0.png",key="BUTTON-9", border_width=0),
    ],
    [sg.VPush()],
    [sg.Button(image_filename = "assets/shuffle.png",key="shuffle" ,border_width=0),
    sg.Button(image_filename = "assets/solution.png",key="resolve" ,border_width=0),
    #sg.Button(image_filename = "assets/setting.png", border_width=0),
    ],
]

directory = "assets/numero-"
extension = ".png"

def transition(t,sommet_initial):
    graph = construct_graph(t)
    #print(graph)
    print("\tEffectué")
# récupérer la valeur de départ du noeud de Taquin
    t.set_node(sommet_initial)
    print("parcours en largeur de la graphe")
    
    liste_bfs = bfs_taquin(graph,t)
    print("\tEffectué")
    print("Résolution du jeu")
    solution = resolve(liste_bfs,sommet_initial)
    represent_solution(solution)
    print("\tRésolu")
    return solution



def update(window,node):
    window["BUTTON-1"].update(image_filename=directory+str(node[0][0])+extension)
    window["BUTTON-2"].update(image_filename=directory+str(node[0][1])+extension)
    window["BUTTON-3"].update(image_filename=directory+str(node[0][2])+extension)
    window["BUTTON-4"].update(image_filename=directory+str(node[1][0])+extension)
    window["BUTTON-5"].update(image_filename=directory+str(node[1][1])+extension)
    window["BUTTON-6"].update(image_filename=directory+str(node[1][2])+extension)
    window["BUTTON-7"].update(image_filename=directory+str(node[2][0])+extension)
    window["BUTTON-8"].update(image_filename=directory+str(node[2][1])+extension)
    window["BUTTON-9"].update(image_filename=directory+str(node[2][2])+extension)

window = sg.Window("Taquin",layout,size=(320,320),element_justification='c')

def main():
    t = Taquin()
    node = t.get_node()
    # main loop
    running = True 
    while running:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'exit':
                running = False
            elif event =="shuffle":
                t.shuffle()
                node = t.get_node()
                update(window,node)
            elif event =="resolve":
                print("display node")
                solution = transition(t,node)
                n = len(solution)
                for i in range(n):
                    update(window,solution[n-i-1])
                    window.refresh()
                    time.sleep(1)
                for key in window.AllKeysDict:
                    window[key].update(button_color='yellow') 
            else:
               pass

    window.close()

if __name__=="__main__":
    main()