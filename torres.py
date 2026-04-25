import pygame
from constantes import *
import math

#TORRES
TIPOS_TORRES = [
    {'Nome': 'Fazendeiro', 'Custo': 50},
    {'Nome': 'Arqueiro', 'Custo': 100},
    {'Nome': 'Cavaleiro', 'Custo': 100}
]

#TORRES
class Torres:
    def __init__(self, posicao_x, posicao_y, altura_torre, tipo):
        self.x = posicao_x
        self.y = posicao_y
        self.altura_torre = altura_torre
        self.y = posicao_y + (120 / 2) - (altura_torre / 2)
        self.tipo = tipo

    def desenhar(self, tela):
        if self.tipo == 'Arqueiro':
            #corpo
            pygame.draw.circle(tela, CORPO_VERDE_CLARO, [self.x+35, self.y+25], 30)
            pygame.draw.circle(tela, CORPO_VERDE_ESCURO, [self.x+30, self.y+25], 25)
            pygame.draw.circle(tela, PELE_TORRE, [self.x+32, self.y+25], 12)
            #item
            pygame.draw.arc(tela, MARROM_TERRA, [self.x+60, self.y, 16, 50],-math.radians(90), -math.radians(270),2)
            pygame.draw.line(tela, CINZA, (self.x+65, self.y+5), (self.x+65, self.y+45), 1)
        elif self.tipo == 'Fazendeiro':
            #corpo
            pygame.draw.circle(tela, CORPO_FAZENDEIRO, [self.x+43, self.y+25], 30)
            pygame.draw.circle(tela, CHAPEU_FAZENDEIRO, [self.x+35, self.y+25], 25)
            pygame.draw.circle(tela, COPA_CHAPEU, [self.x+35, self.y+25], 10)
            #item
            pygame.draw.line(tela, MARROM_MADEIRA, (self.x+45, self.y-5), (self.x+65, self.y-25),4)
        elif self.tipo == 'Cavaleiro':
            #corpo
            pygame.draw.circle(tela, CORPO_CAVALEIRO, [self.x+43, self.y+25], 36)
            pygame.draw.circle(tela, CAPACETE, [self.x+35, self.y+25], 28)
            pygame.draw.rect(tela, VISEIRA_CLARA, (self.x+37, self.y+14, 15, 25))
            pygame.draw.rect(tela, VISEIRA_ESCURA, (self.x+39, self.y+17, 9, 17))
            pygame.draw.ellipse(tela, PLUMA, (self.x+15, self.y+20, 20, 7))
            #item
            pygame.draw.ellipse(tela, MARROM_TERRA, (self.x+75, self.y, 10, 50))
            pygame.draw.ellipse(tela, MARROM_MADEIRA, (self.x+78, self.y+8, 10, 30))