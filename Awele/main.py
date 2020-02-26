#!/usr/bin/env python
# -*- coding: utf-8 -*-
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain

def joue():
    jeu=game.initialiseJeu()
    it=0
    while(it<100) and not game.finJeu(jeu):
        game.affiche(jeu)
        coup=game.saisieCoup(jeu)
        game.joueCoup(jeu,coup)
        it+=1
    game.affiche(jeu)
    print ("Gagnant="+str(game.getGagnant(jeu))+":"+str(game.getScore(jeu)))
    return jeu

jeu=game.initialiseJeu()
game.affiche(jeu)
