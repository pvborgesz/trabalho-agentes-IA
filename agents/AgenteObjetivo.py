from agents.AgenteGenerico import AgenteGenerico

acoes = []
percepcoes = []
localizacao = []

# AgenteGenerico = AgenteGenerico.AgenteGenerico(acoes, percepcoes, localizacao)

class AgenteObjetivo(AgenteGenerico):
    def __init__(self, acoes, percepcoes, localizacao,collectedPoints):
        # super().__init__()
        self.acoes = acoes
        self. percepcoes = percepcoes
        self.localizacao = localizacao
        self.collectedPoints = collectedPoints
        self.posX = localizacao[0]
        self.posY = localizacao[1]
        self.hasItem = False
        self.mapa = []
        self.lastPosition = []

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

    def getPosition(self):
        return [self.posX, self.posY]

    def setPosition(self, pos):
        self.posX = pos[0]
        self.posy = pos[1]

    def getHasItem(self):
        return self.hasItem
    
    def setHasItem(self, hasItem):
        self.hasItem = hasItem   

    def getCollectedPoints(self):
        return self.collectedPoints

    def setCollectedPoints(self, collectedPoints):
        self.collectedPoints = collectedPoints   

    def setMapa(self, mapa):
        self.mapa = mapa
    def getMapa(self):
        return self.mapa    
    
    def getLastPosition(self):
        return [self.posX, self.posY]

    def setLastPosition(self, pos):
        self.posX = pos[0]
        self.posy = pos[1]


    def mapearSpace(self,space):
        posicaoPontos = []
        for i in range (len(space)):
            for j in range (len(space)):
                if (space[i][j] == 'azul' or space[i][j] == 'vermelho'):
                    posicaoPontos.append([i,j])
                    # posicaoPontos.append([i,j, space[i][j]])

        aux = 0 
        maiorVetor = []
        for i in posicaoPontos:
            if (i[1] > aux):
                maiorVetor.append(i)
                aux = i[1]

        # print("Encontrei pontos nos locais: ", posicaoPontos, "total de pontos: ", len(posicaoPontos))
        return maiorVetor           

    def gotoPoint(self, posPoints, space, agente):
        currentPosition = agente.getPosition()

        x = currentPosition[0]
        y = currentPosition[1]
        # print(posPoints)
        posPoints.sort()

        for i in range(len(posPoints)):
            while (x != posPoints[0][0]):
                x += 1
                print('andei p direita')
            while (y != posPoints[0][1]):
                y += 1
                print('andei p baixo')
        posPoints.pop(0)       

        agente.setPosition([x,y])
        
        return;
