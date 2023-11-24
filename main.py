# Importer le module qui contient toutes les
# fonctionnalités python pygame.
import pygame

# initialiser toutes les fonctionnalités.
pygame.init()

# initialiser l'image backround
backround = pygame.image.load("assets/bg.jpg")

# generer la fenêtre de notre jeu
pygame.display.set_caption("Cool Game")
pygame.display.set_mode((800, 600))

running = True

# on crée une looop infinie pour garder la fenetre ouverte
while running:

    #on affiche l'image de bakcround a l'ecran
    screen.blit(backround, (0, 0))

    #mettre l'ecran a jour
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

