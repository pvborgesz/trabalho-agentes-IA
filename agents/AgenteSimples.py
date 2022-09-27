from agents.AgenteGenerico import AgenteGenerico

acoes = []
percepcoes = []
localizacao = []

# AgenteGenerico = AgenteGenerico.AgenteGenerico(acoes, percepcoes, localizacao)

class AgenteSimples(AgenteGenerico):
    def __init__(self, acoes, percepcoes, localizacao,collectedPoints, posX, posY):
        # super().__init__()
        self.acoes = acoes
        self. percepcoes = percepcoes
        self.localizacao = localizacao
        self.collectedPoints = collectedPoints
        self.posX = posX
        self.posY = posY

     #Define o movimento de subir
    def cima(self):
        if self.y - 1 >= 0: #Verifica se não irá sair para fora do mapa
            self.y -= 1     
    #Define o movimento de descer
    def baixo(self):
        if self.y + 1 < self.Ambiente.m : # Verifica se irá sair para fora do mapa
            self.y += 1
    #Define o movimento de ir para Esquerda
    def esquerda(self):
        if self.x - 1 >= 0:
            self.x -= 1
    def direita(self):
        if self.x + 1 < self.Ambiente.n:
            self.x += 1