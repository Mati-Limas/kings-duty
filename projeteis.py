import pygame


class Projetil:
    def __init__(self, x, y, alvo):
        self.x = x
        self.y = y
        self.velocidade = 5
        self.dano = 25
        self.ativo = True
        self.alvo = alvo

    def mover(self):
        if self.ativo:
            self.x += self.velocidade

    def desenhar(self,tela):
        fileira = self.y
        distancia = self.x
        pygame.draw.line(tela, (220, 50,50), (distancia, fileira+20), (distancia+15, fileira+20))
        pygame.draw.polygon(tela, (50, 50, 50), ((distancia+15, fileira+10), (distancia+15, fileira+30),
                                                 (distancia+30, fileira+20)))

    def verificar_colisao(self):
        if self.ativo and self.alvo.vivo and self.x >= self.alvo.posicao_x:
            self.alvo.receber_dano(self.dano)
            self.ativo = False
            return True
        return False