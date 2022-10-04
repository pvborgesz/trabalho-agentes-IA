from agents.AgenteGenerico import AgenteGenerico
acoes = []
percepcoes = []
localizacao = []

# from numpy import numpy as np

# AgenteGenerico = AgenteGenerico.AgenteGenerico(acoes, percepcoes, localizacao)

class AgenteUtilidade(AgenteGenerico):
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
                if (space[i][j] == 'B ' or space[i][j] == 'R '):
                    # posicaoPontos.append([i,j])
                    posicaoPontos.append([i,j, space[i][j]])

        print(posicaoPontos)
        # print("Encontrei pontos nos locais: ", posicaoPontos, "total de pontos: ", len(posicaoPontos))
        return posicaoPontos        

    def gotoPoint(self, posPoints, space, agente):
        currentPosition = agente.getPosition()

        x = currentPosition[0]
        y = currentPosition[1]

        for i in range(len(posPoints)):
            while (x != posPoints[0][0]):
                x += 1
                # print('andei p direita')
                if (space[x][y] == 'R ' or space[x][y] == 'azul '):
                    collectPoint([x,y], space[x][y], agente,space)
            while (y != posPoints[0][1]):
                y += 1
                # print('andei p baixo')
                if (space[x][y] == 'R ' or space[x][y] == 'azul '):
                    collectPoint([x,y], space[x][y], agente,space)

        posPoints.pop(0)       

        agente.setPosition([x,y])
        
        return;

    def collectPoint(positionPoint, pointColor, agente,space): 
        x = positionPoint[0]
        y = positionPoint[1]
        if (agente.getHasItem() == False) :
            if (pointColor == 'R '): 
                space[x][y] = '0'
                agente.setCollectedPoints(agente.getCollectedPoints() + 10)
                agente.setHasItem(True)
                printSpace(space)
                returnBase(agente)
                print("minha pontuacao atual é de: ", agente.getCollectedPoints())
                return True
            elif (pointColor == 'B '): 
                space[x][y] = '0'
                agente.setCollectedPoints(agente.getCollectedPoints() + 20)
                agente.setHasItem(True)
                printSpace(space)
                returnBase(agente)
                print("minha pontuacao atual é de: ", agente.getCollectedPoints())
                return True
        
        # printSpace(space)
        if (isinstance(agenteCModelos, AgenteCModelos)):
            agente.setLastPosition(x,y)
            print ("oi, sou o agente e coletei em ", agente.getLastPosition())
        print("minha pontuacao atual é de: ", agente.getCollectedPoints())
