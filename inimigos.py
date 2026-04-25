from constantes import *
import pygame

class Inimigos:
    def __init__(self, posicao_x: int, posicao_y: int, velocidade: int, hp: int, tipo: str):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade = velocidade
        self.hp_atual = hp
        self.hp_maximo = hp
        self.fileira = 120 + ((posicao_y - 120) // 120) * 120 + 60
        self.tipo = tipo
        self.vivo = True

    def mover(self):
        self.posicao_x -= self.velocidade

    def desenhar(self, tela):
        pygame.draw.circle(tela, VERDE_ORC, (self.posicao_x, self.fileira), 35)

    def receber_dano(self, dano):
        self.hp_atual -= dano
        if self.hp_atual <= 0:
            self.vivo = False

