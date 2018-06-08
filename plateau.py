

def affichage(plateau):
    for v in plateau :
        print(str(v).replace("''","[ ]").replace(",",""))

def numeroLigne(colonne, plateau):
    vides = -1
    for vLigne in plateau:
        if vLigne[colonne] == "":
            vides += 1
    return vides

def joue(colonne, plateau) :
    ligne = int(numeroLigne(colonne, plateau))
    if ligne > -1 :
        plateau[ligne][colonne] = "0"
    else :
        print("colonne pleine")
    return plateau[ligne][colonne]

def verif(colonne, plateau, ligne):
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, 1], [1, -1], [-1, -1], [1, 1]]
    curentCase = [colonne, ligne]
    vertical, horizontal, diag1, diag2 = 1, 1, 1, 1
    for d in directions :
        for icurent in range(1, 5):

            k = abs(int(d[0]))*(icurent) if int(d[0]) > 0 else - (abs(int(d[0]))*(icurent))
            l = abs(int(d[1]))*(icurent) if int(d[1]) > 0 else - (abs(int(d[1]))*(icurent))

            c1 = curentCase[0] + k
            c2 = curentCase[1] + l 
            verifCase = [c1, c2]
            if verifCase == curentCase or verifCase in bord(plateau):
                print("xx ", k, l, c1, c2)
                break
            else :
                horizontal = horizontal+1 if curentCase == directions[0] or curentCase == directions[1] else horizontal
                vertical = vertical +1 if curentCase == directions[2] or curentCase == directions[3] else vertical
                diag1 = diag1 +1 if curentCase == directions[4] or curentCase == directions[5] else diag1
                diag2 = diag2 +1 if curentCase == directions[6] or curentCase == directions[7] else diag2
                print(horizontal, vertical, diag1, diag2)
                print("ok ", k, l, c1, c2)

def bord(plateau):
    bord = [[i, j] for i in range(-1, 7+1) for j in range(-1, 6+1) if i == -1 or j == -1 or i ==  7 or j == 6]
    #print(bord)
    return bord
        
plateau = [["" for i in range(7)] for j in range(6)]


affichage(plateau)
bord(plateau)
for i in range(0, 15):
    colonne = int(input("colonne ? "))
    joue(colonne, plateau)
    affichage(plateau)
    verif(colonne, plateau, numeroLigne(colonne, plateau)+1)



# def verif(colonne, plateau, ligne):
#     vertical, horizontal, diag1, diag2 = 0, 0, 0, 0
#     longueurP = len(plateau[0])
#     a = plateau[ligne][colonne]

#     maxi = ( longueurP - colonne ) if ( longueurP - colonne ) < 6 else 5
#     mini = - (longueurP - ( longueurP - colonne )) if longueurP - ( longueurP - colonne ) < 6 else 5
#     print(longueurP, ligne, colonne, -mini, maxi)
#     horizontal = verifHorizontale(colonne, plateau, ligne, a, mini, maxi, horizontal)
#     total = max(vertical, horizontal, diag1, diag2)
#     print(total)
#     return total

# def verifHorizontale(colonne, plateau, ligne, a, mini, maxi, horizontal):

#     for iAvant in range(0, maxi):
#         icol = colonne + iAvant
#         b = plateau[ligne][icol]
#         if a == b :
#             horizontal +=1
#         else :
#             break
#     for iArriere in range(-1, mini, -1):
#         jcol = colonne + iArriere
#         b = plateau[ligne][jcol]
#         if a == b :
#             horizontal +=1
#         else : 
#             break

#     return horizontal
