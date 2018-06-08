

def affichage(plateau, curentJoueur = ""):
    for v in plateau :
        print(str(v).replace("''","[ ]").replace(",",""))
    print("-----------------------------")
    print("  1   2   3   4   5   6   7   : index colonnes")
    

def numeroLigne(colonne, plateau):
    vides = -1
    for vLigne in plateau:
        if vLigne[colonne] == "":
            vides += 1
    return vides

def joue(colonne, plateau, valeur) :
    ligne = int(numeroLigne(colonne, plateau))
    if ligne > -1 :
        plateau[ligne][colonne] = str(valeur)
    else :
        print("colonne pleine")
    return plateau[ligne][colonne]

def verif(colonne, plateau, ligne):

    directions = [[0, -1], [-1, 0], [-1, 1], [-1, -1]]
    curentCase = [ligne, colonne]
    compteurs = [1, 1, 1, 1]
    sens = range(2)
    for d in directions :
        for s in sens :
            d = [i*-1 for i in d]
            for icurent in range(1, 5):        

                c1 = curentCase[0] + d[0] * icurent
                c2 = curentCase[1] + d[1] * icurent
                verifCase = [c1, c2]

                if verifCase in bord(plateau) or plateau[ligne][colonne] != plateau[c1][c2]:
                    # print("xx ", k, l, c1, c2)
                    break
                else :
                    # print(plateau[ligne][colonne], plateau[int(c1)][int(c2)])
                    for icompteur, vcompteur in enumerate(directions):
                        for s in sens :
                            vcompteur = [i*-1 for i in vcompteur]
                            if d == vcompteur:
                                compteurs[icompteur] = compteurs[icompteur] + 1 
                        # print(compteurs)
                        
                    # print("ok ", c1, c2)
    return compteurs

def victoire(compteur):
    if 4 in compteur:
        print("félicitation !!")

def bord(plateau):
    bord = [[j, i] for i in range(-1, 7+1) for j in range(-1, 6+1) if i == -1 or j == -1 or i ==  7 or j == 6]
    #print(bord)
    return bord
        

def joueur(numJoueur, nbJoueurs):

    # joueurs = []
    # for i in nbJoueurs:
    #     joueurs.append("joueur"+i)
    curentJoueur = "joueur" + str(numJoueur+1) if numJoueur < nbJoueurs else "joueur" + str(1)
    numJoueur = numJoueur +1 if numJoueur < nbJoueurs else 1
    # print(curentJoueur)
    rslt = [curentJoueur, numJoueur]
    return rslt


    


plateau = [["" for i in range(7)] for j in range(6)]
nbJoueurs = int(input("nombre de joueurs : "))
numJoueur = 0
# compteur = [1, 1, 1, 1]
affichage(plateau)
bord(plateau)
compteur = [0, 0, 0, 0]
while not 4 in compteur:

    rslt = joueur(numJoueur, nbJoueurs)
    curentJoueur = rslt[0]
    numJoueur = rslt[1]
    print(curentJoueur)

    colonne = int(input("colonne ? ")) - 1
    joue(colonne, plateau, numJoueur)
    affichage(plateau, curentJoueur)
    compteur = verif(colonne, plateau, numeroLigne(colonne, plateau)+1)
    victoire(compteur)


