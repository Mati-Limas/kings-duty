
#TELA PRINCIPAL
LARGURA=900
ALTURA=725

#INFO HUD
LARGURA_BARRA=400
HP_CASTELO=100
hp_atual=100
ouro=100

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

#CORES INIMIGOS
VERDE_ORC = (85, 107, 47)
#CORES TORRES
#arqueiro
CORPO_VERDE_CLARO = (110, 180, 90)
CORPO_VERDE_ESCURO = (50, 120, 50)
#fazendeiro
CORPO_FAZENDEIRO = (196, 135, 58)
CHAPEU_FAZENDEIRO = (212,168,75)
COPA_CHAPEU = (184, 137, 46)
PELE_TORRE = (205, 160, 115)
#cavaleiro
CORPO_CAVALEIRO = (128, 144, 168)
CAPACETE = (106, 120, 136)
VISEIRA_CLARA = (58, 72, 88)
VISEIRA_ESCURA = (26, 40, 56)
PLUMA = (200, 48, 48)

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