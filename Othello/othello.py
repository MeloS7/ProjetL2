#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import game

def initialiseJeu():
    
    nbLigne=8
    nbCol=8
    listCoupPossible=[]
    listCoupJoue=[]
    pairScore=[0,0]
    plateau=[[" "]*nbLigne]*nbCol
    
    return [plateau,1,listCoupPossible,listCoupJoue,pairScore]

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
        On suppose que la fonction n'est appelee que si il y a au moins un coup valide possible
        et qu'elle retourne obligatoirement un coup valide
    """
    if len(jeu[2]):
        x,y=input("saisie la coordonnee du coup(x,y):")
        
        
    
def getCoupsValides(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups valides dans le jeu passe en parametre
        Si None, alors on met � jour la liste des coups valides
    """
    
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
    print "      |   0  |   1  |   2  |   3  |   4  |   5  |   6  |   7  |     "   
    print "---------------------------------------------------------------"
    
    ligne=0
    while(ligne<game.getNbLignes(jeu)):
        print("  "+str(ligne)+"  "),
        colonne=0
        while(colonne<game.getNbColonnes(jeu)):
            print("|  "+str(jeu[0][ligne][colonne])+"  "),
            colonne+=1
        print "|"
        print "---------------------------------------------------------------"
        ligne+=1
        
    if jeu[1]==1:
        print "Joueur <Joueur1>, a vous de jouer"
    elif jeu[1]==2:
        print "Joueur <Joueur2>, a vous de jouer"
    else:
        print "Erreur!"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
