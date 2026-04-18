import pygame

pygame.init()

#TELA PRINCIPAL
LARGURA=900
ALTURA=725

#INFO HUD
LARGURA_BARRA=400
HP_CASTELO=100
hp_atual=100
ouro=100
FONTE=pygame.font.SysFont('Arial', 28, True)

#TORRES
TIPOS_TORRES = [
    {'Nome': 'Fazendeiro', 'Custo': 50},
    {'Nome': 'Arqueiro', 'Custo': 100},
    {'Nome': 'Cavaleiro', 'Custo': 100}
]
#FILEIRAS/GRID
FILEIRAS = [120,240,360,480]
X_GRID = 150
Y_GRID = 120
GRID = {}
DENTRO_GRID = False
COLUNAS=10
LINHAS=4
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        x = X_GRID + coluna * 75
        y = Y_GRID + linha * 120
        GRID[(linha, coluna)] = {
            'x': x,
            'y': y,
            'ocupado': False,
            'torre': None
        }

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

#CORES
#cores campo
VERDE_CLARO = (80, 160, 60)
VERDE_ESCURO = (34, 100, 34)

#cor castelo
CINZA = (120, 120, 120)

#cor HUD
MARROM_TERRA = (139, 69 ,19)
MARROM_MADEIRA = (92, 51, 23)
VERMELHO = (220, 50, 50)
DOURADO = (212, 175, 55)

#cor céu
AZUL = (135, 206, 235)

#CORES TORRES
CORPO_VERDE_CLARO = (110, 180, 90)
CORPO_VERDE_ESCURO = (50, 120, 50)
CORPO_FAZENDEIRO = (196, 135, 58)
CHAPEU_FAZENDEIRO = (212,168,75)
COPA_CHAPEU = (184, 137, 46)
PELE_TORRE = (205, 160, 115)
CORPO_CAVALEIRO = (128, 144, 168)
CAPACETE = (106, 120, 136)
VISEIRA_CLARA = (58, 72, 88)
VISEIRA_ESCURA = (26, 40, 56)
PLUMA = (200, 48, 48)

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
        elif self.tipo == 'Fazendeiro':
            #corpo
            pygame.draw.circle(tela, CORPO_FAZENDEIRO, [self.x+43, self.y+25], 30)
            pygame.draw.circle(tela, CHAPEU_FAZENDEIRO, [self.x+35, self.y+25], 25)
            pygame.draw.circle(tela, COPA_CHAPEU, [self.x+35, self.y+25], 10)
        elif self.tipo == 'Cavaleiro':
            #corpo
            pygame.draw.circle(tela, CORPO_CAVALEIRO, [self.x+43, self.y+25], 36)
            pygame.draw.circle(tela, CAPACETE, [self.x+35, self.y+25], 28)
            pygame.draw.rect(tela, VISEIRA_CLARA, (self.x+37, self.y+14, 15, 25))
            pygame.draw.rect(tela, VISEIRA_ESCURA, (self.x+39, self.y+17, 9, 17))
            pygame.draw.ellipse(tela, PLUMA, (self.x+15, self.y+20, 20, 7))

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