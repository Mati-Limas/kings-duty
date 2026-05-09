from constantes import *
import pygame

class Inimigos:
    def __init__(self, posicao_x: int, posicao_y: int, tipo: str):
        dados = TIPOS_INIMIGOS[tipo]
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade = dados['velocidade']
        self.hp_atual = dados['hp']
        self.hp_maximo = dados['hp']
        self.dano = dados['dano']
        self.fileira = 120 + ((posicao_y - 120) // 120) * 120 + 60
        self.tipo = tipo
        self.vivo = True
        self.chegou = False

    def mover(self):
        self.posicao_x -= self.velocidade
        if self.posicao_x <= 150:
            self.vivo = False
            self.chegou =  True


    def desenhar(self, tela):
        if self.tipo == 'orc':
            pygame.draw.circle(tela, VERDE_ORC, (self.posicao_x, self.fileira), 35)
        elif self.tipo == 'troll':
            pygame.draw.circle(tela, VERDE_ORC, (self.posicao_x, self.fileira), 50)

    def receber_dano(self, dano):
        self.hp_atual -= dano
        if self.hp_atual <= 0:
            self.vivo = False

