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
        self.y_fileira = (posicao_y - 120) // 120
        self.tipo = tipo
        self.vivo = True
        self.chegou = False
        self.block = False
        self.cooldown_atk = 60

    def atacar(self, torre):
        self.cooldown_atk -= 1
        if self.cooldown_atk == 0:
            torre.vida -= self.dano
            torre.timer_dano = 10
            self.cooldown_atk = 60
    def mover(self):
        if not self.block:
            self.posicao_x -= self.velocidade
            if self.posicao_x <= 150:
                self.vivo = False
                self.chegou =  True


    def desenhar(self, tela):
        x = self.posicao_x
        y = self.fileira
        if self.tipo == 'orc':
            # CORPO
            pygame.draw.circle(tela, VERDE_ORC, (x, y), 45)
            # OLHOS
            pygame.draw.circle(tela, VERDE_OLHOS, (x - 12, y - 10), 6)
            pygame.draw.circle(tela, VERDE_OLHOS, (x - 12, y + 10), 6)
            # BRILHO DOS OLHOS
            pygame.draw.circle(tela, (90, 120, 90), (x - 14, y - 12), 2)
            pygame.draw.circle(tela, (90, 120, 90), (x - 14, y + 8), 2)
            # PRESAS
            pygame.draw.polygon(tela, BRANCO_PRESAS, [
                (x - 27, y - 13),
                (x - 39, y - 8),
                (x - 27, y + 4)
            ])
            pygame.draw.polygon(tela, BRANCO_PRESAS, [
                (x - 27, y + 13),
                (x - 39, y + 8),
                (x - 27, y - 4)
            ])
        elif self.tipo == 'troll':
            # CORPO
            pygame.draw.circle(tela, VERDE_ORC, (x, y), 68)
            # OMBROS
            pygame.draw.circle(tela, VERDE_ORC, (x - 30, y - 35), 28)
            pygame.draw.circle(tela, VERDE_ORC, (x - 30, y + 35), 28)
            # OLHOS SANGUINÁRIOS
            pygame.draw.circle(tela, VERMELHO_DESATURADO, (x - 15, y - 15), 8)
            pygame.draw.circle(tela, VERMELHO_DESATURADO, (x - 15, y + 15), 8)
            # PRESAS GIGANTES
            pygame.draw.polygon(tela, BRANCO_PRESAS, [
                (x - 35, y - 12),
                (x - 55, y - 5),
                (x - 38, y + 5)
            ])
            pygame.draw.polygon(tela, BRANCO_PRESAS, [
                (x - 35, y + 12),
                (x - 55, y + 5),
                (x - 38, y - 5)
            ])
            # TACAPE GIGANTE
            pygame.draw.line(
                tela,
                TACAPE,
                (x - 130, y - 70),
                (x - 40, y - 20),
                18
            )
            # CABEÇA DA ARMA
            pygame.draw.circle(tela, TACAPE, (x - 135, y - 75), 30)
            # METAL / PEDRA
            pygame.draw.circle(tela, CINZA_ESCURO, (x - 135, y - 75), 18)
        elif self.tipo == 'veloz':
            # CORPO
            pygame.draw.circle(tela, VERDE_AZULADO_VELOZ, (x, y), 30)
            # OLHOS
            pygame.draw.circle(tela, VERMELHO_DESATURADO, (x - 10, y - 8), 4)
            pygame.draw.circle(tela, VERMELHO_DESATURADO, (x - 10, y + 8), 4)
            # MARCAÇÃO NAS COSTAS
            pygame.draw.circle(tela, (170, 120, 110), (x + 8, y), 8, 2)
        elif self.tipo == 'cavaleiro':
            # CORPO
            pygame.draw.circle(tela, VERDE_ORC, (x, y), 55)
            # ARMADURA
            pygame.draw.circle(tela, CINZA_ARMADURA, (x - 5, y), 35)
            # CENTRO ARMADURA
            pygame.draw.circle(tela, CINZA_ESCURO, (x - 5, y), 15)
            # OLHOS
            pygame.draw.circle(tela, VERMELHO_DESATURADO, (x - 12, y - 10), 5)
            pygame.draw.circle(tela, VERMELHO_DESATURADO, (x - 12, y + 10), 5)
            # PRESAS
            pygame.draw.polygon(tela, BRANCO_PRESAS, [
                (x - 35, y - 15),
                (x - 49, y - 9),
                (x - 35, y + 3)
            ])
            pygame.draw.polygon(tela, BRANCO_PRESAS, [
                (x - 35, y + 15),
                (x - 49, y + 9),
                (x - 35, y - 3)
            ])
            # TACAPE
            pygame.draw.line(
                tela,
                TACAPE,
                (x - 90, y - 45),
                (x - 30, y - 15),
                12
            )
            # CABEÇA DO TACAPE
            pygame.draw.circle(tela, TACAPE, (x - 95, y - 50), 18)
            # ESPINHOS
            pygame.draw.polygon(tela, BRANCO_PRESAS, [
                (x - 105, y - 60),
                (x - 115, y - 70),
                (x - 100, y - 68)
            ])

    def receber_dano(self, dano):
        self.hp_atual -= dano
        if self.hp_atual <= 0:
            self.vivo = False

