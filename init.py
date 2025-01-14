from game_of_life import Game_of_life
game = Game_of_life()

size = int(input('Veuillez entrer la taille de la grille (par exemple, 100 pour une grille 100x100) :\n'))
pop = float(input('Quelle proportion de cellules vivantes initiales souhaitez-vous ? (entre 0 et 1, par exemple 0.2 pour 20%) :\n'))
game.__init__(size)
iterations = int(input('Combien de cycles d\'itérations voulez-vous que le jeu exécute ? (par exemple, 50) :\n'))
game.run(iterations)