# -*- coding: utf-8 -*-

pip install pygame

import pygame
import sys

# Définir les constantes pour la fenêtre
LARGEUR = 30*n
HAUTEUR = 20*m
TAILLE_CELLULE = 20
ROWS = HAUTEUR // TAILLE_CELLULE
COLS = LARGEUR // TAILLE_CELLULE

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (150, 150, 150)

def draw_grid(surface): # tracer de la grille vierge 
    for y in range(0, HAUTEUR, TAILLE_CELLULE):
        pygame.draw.line(surface, GRIS, (0, y), (LARGEUR, y))
    for x in range(0, LARGEUR, TAILLE_CELLULE):
        pygame.draw.line(surface, GRIS, (x, 0), (x, HAUTEUR))

def get_cell(pos): # renvoie la position d'une case
    x, y = pos
    row = y // TAILLE_CELLULE
    col = x // TAILLE_CELLULE
    return row, col

def table(): # créer la table en la remplissant des valeurs du tableau
    pygame.init()
    screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Tableau avec Pygame")

    grid = [[0 for n in range(COLS)] for m in range(ROWS)]  
    for row in range(ROWS):
            for col in range(COLS):
                value = str(grid[n][m])  
                font = pygame.font.Font(None, 20)
                text_surface = font.render(value, True, NOIR)
                text_rect = text_surface.get_rect(center=(col * TAILLE_CELLULE + TAILLE_CELLULE // 2, row * TAILLE_CELLULE + TAILLE_CELLULE // 2))
                screen.blit(text_surface, text_rect)

    pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__table__":
    table()