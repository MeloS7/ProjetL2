#! /usr/bin/env python3
print "hello"
print "a little change"
print
print "The 4th change"
print (123)

tab=[["1"]*5]*6
print tab

jeu1=[tab,1,[],[],[0,0]]

def getNbLignes(jeu):
    return len(jeu[0])
    
def getNbColonnes(jeu):
    return len(jeu[0][0])


print ("le nbLignes:"+str(getNbLignes(jeu1)))
print ("le nbColonnes:"+str(getNbColonnes(jeu1)))

'''
def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer
                    
         Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """
    #afficher la premiere ligne
    print "     |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |     "   
    print "-----------------------------------------------------------"
    
    ligne=0
    while(ligne<getNbLignes(jeu)):
        print("  "+str(ligne)+"  "),
        colonne=0
        while(colonne<getNbColonnes(jeu)):
            print("|  "+str(jeu[0][ligne][colonne])+"  "),
            colonne+=1
        print
        print "-----------------------------------------------------------"
        ligne+=1
affiche(jeu1)
'''
