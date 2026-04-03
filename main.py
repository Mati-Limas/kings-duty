import pygame

pygame.init()

LARGURA=900
ALTURA=725
LARGURA_BARRA=400
HP_CASTELO=100
hp_atual=100
ouro=100
FONTE=pygame.font.SysFont('Arial', 28, True)

tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Kings Duty')
clock = pygame.time.Clock()

#CORES
VERDE_CLARO = (80, 160, 60)
VERDE_ESCURO = (34, 100, 34)

CINZA = (120, 120, 120)

MARROM_TERRA = (139, 69 ,19)
MARROM_MADEIRA = (92, 51, 23)

AZUL = (135, 206, 235)

VERMELHO = (220, 50, 50)

DOURADO = (212, 175, 55)



rodando = True

while rodando:
    mensagem = f'{ouro}'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill(AZUL)

    #CASTELO
    pygame.draw.rect(tela, CINZA, (0, 120, 150, 480))

    #CAMPO
    pygame.draw.rect(tela, VERDE_ESCURO, (150, 120, 750, 120))
    pygame.draw.rect(tela, VERDE_CLARO, (150, 240, 750, 120))
    pygame.draw.rect(tela, VERDE_ESCURO, (150, 360, 750, 120))
    pygame.draw.rect(tela, VERDE_CLARO, (150, 480, 750, 120))

    #HUD
    proporcao_vida = hp_atual / HP_CASTELO
    largura_barra = LARGURA_BARRA * proporcao_vida
    pygame.draw.rect(tela, MARROM_MADEIRA, (0,600, 900, 125))
    pygame.draw.rect(tela, MARROM_MADEIRA, (0,0, 900, 80))
    pygame.draw.rect(tela, VERMELHO, (250, 20, largura_barra, 40))
    pygame.draw.circle(tela, DOURADO, (100, 40), 20)
    texto = FONTE.render(mensagem, False, DOURADO)
    tela.blit(texto, (135, 35))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()