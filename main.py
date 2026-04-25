import pygame
from torres import Torres, TIPOS_TORRES
from constantes import *

pygame.init()

#FONTE
FONTE=pygame.font.SysFont('Arial', 28, True)
#VARIAVEIS NECESSARIAS
torre_selecionada = None
NUM_TORRES = len(TIPOS_TORRES)
LARGURA_BOTAO = (750 - 10 * (NUM_TORRES + 1)) / NUM_TORRES
def x_botao(i):
    return 150 + 10 + i * (LARGURA_BOTAO + 10)
torres_ativas = []


tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Kings Duty')
clock = pygame.time.Clock()
rodando = True

while rodando:
    mensagem = f'{ouro}'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos() #
            if 605 <= mouse_y <= 705 and 150 <= mouse_x <= 890:
                for i, torre in enumerate(TIPOS_TORRES):
                    if x_botao(i) <= mouse_x <= x_botao(i)+LARGURA_BOTAO:
                        torre_selecionada = torre['Nome']
                        break

            if DENTRO_GRID and torre_selecionada is not None:
                coluna = (mouse_x - 150) // 75
                linha = (mouse_y - 120) // 120
                celula = GRID[(linha, coluna)]
                if not GRID[(linha,coluna)]['ocupado']:
                    torres_ativas.append(Torres(celula['x'],celula['y'],60,torre_selecionada))
                    GRID[(linha,coluna)]['ocupado'] = True
                    torre_selecionada = None




    #LER MOUSE 120-600 150-900
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    coluna = (mouse_x - 150) // 75
    linha = (mouse_y - 120) // 120
    if 900 >= mouse_x >= 150 and 600 >= mouse_y >= 120:
        DENTRO_GRID = True
    else:
        DENTRO_GRID = False


    #SEÇÃO DE DESENHO
    tela.fill(AZUL)

    #CASTELO
    pygame.draw.rect(tela, CINZA, (0, 120, 150, 480))

    #CAMPO
    pygame.draw.rect(tela, VERDE_ESCURO, (150, 120, 750, 120))
    pygame.draw.rect(tela, VERDE_CLARO, (150, 240, 750, 120))
    pygame.draw.rect(tela, VERDE_ESCURO, (150, 360, 750, 120))
    pygame.draw.rect(tela, VERDE_CLARO, (150, 480, 750, 120))

    #TORRES
    for torre in torres_ativas:
        torre.desenhar(tela)

    #HUD
    proporcao_vida = hp_atual / HP_CASTELO
    largura_barra = LARGURA_BARRA * proporcao_vida
    pygame.draw.rect(tela, MARROM_MADEIRA, (0,600, 900, 125))
    pygame.draw.rect(tela, MARROM_MADEIRA, (0,0, 900, 80))
    pygame.draw.rect(tela, VERMELHO, (250, 20, largura_barra, 40))
    pygame.draw.circle(tela, DOURADO, (100, 40), 20)
    #BOTÕES DAS TORRES
    for i in range(0,3):
        x = x_botao(i)
        pygame.draw.rect(tela, DOURADO, (x, 605, LARGURA_BOTAO, 100))

    texto = FONTE.render(mensagem, False, DOURADO)
    tela.blit(texto, (135, 35))

    if DENTRO_GRID and 3 >= linha >= 0 and 9 >= coluna >=0:
        X=GRID[(linha, coluna)]['x']
        Y=GRID[(linha, coluna)]['y']
        destaque = pygame.Surface((75,120), pygame.SRCALPHA)
        destaque.fill((255,255,255,80))
        tela.blit(destaque, (X,Y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()