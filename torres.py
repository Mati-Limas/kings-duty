import pygame
from constantes import *
import math

#TORRES
TIPOS_TORRES = [
    {'Nome': 'Fazendeiro', 'Custo': 50, 'hp': 50},
    {'Nome': 'Arqueiro', 'Custo': 100, 'hp': 100},
    {'Nome': 'Cavaleiro', 'Custo': 100, 'hp': 200}
]

#TORRES
class Torres:
    def __init__(self, posicao_x, posicao_y, altura_torre, tipo, hp):
        self.x = posicao_x
        self.y = posicao_y
        self.altura_torre = altura_torre
        self.y = posicao_y + (120 / 2) - (altura_torre / 2)
        self.fileira = (posicao_y - 120) // 120
        self.tipo = tipo
        self.vida = hp
        self.vivo = True
        self.timer = 450
        self.gerou_ouro = False
        self.timer_dano = 0
        self.cooldown_tiro = 0

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
        if self.timer_dano > 0:
            self.timer_dano -= 1
            flash = pygame.Surface((75, 90), pygame.SRCALPHA)
            flash.fill((0, 0, 0, 0))
            pygame.draw.circle(flash, (220, 50, 50, 100), (40, 30), 35)
            tela.blit(flash, (self.x, self.y))
    def gerar_ouro(self):
        self.timer -= 1
        if self.timer == 0:
            self.gerou_ouro = True
            self.timer = 450

    def atirar(self, inimigos: list):
        inimigos_na_fileira = [i for i in inimigos if i.y_fileira == self.fileira and i.vivo]
        if inimigos_na_fileira:
            alvo = min(inimigos_na_fileira, key=lambda i: i.posicao_x)
            return alvo
        else:
            return None