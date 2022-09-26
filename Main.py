import agents.AgenteSimples as AgenteSimples
import agents.AgenteGenerico as AgenteGenerico
import utils.Pontos as geradorPontos
from random import randint
# import numpy as np

def printSpace(positionPoints):
    for i in positionPoints:
        print(i)


class Main:
    # def __init__(self,val):    
    teste = (geradorPontos.geradorPontos())

    acoes = ["andar", "coletar", "retornar"]
    percepcoes = ["ver"]
    localizacao = [0,0] 
    
    agenteSimplesInstance = AgenteGenerico.AgenteGenerico(acoes=acoes, percepcoes=percepcoes, localizacao=localizacao)
    print(len(teste))
