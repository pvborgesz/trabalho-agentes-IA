import agents.AgenteSimples as AgenteSimples
import agents.AgenteGenerico as AgenteGenerico


class Main:
    # def __init__(self,val):
    print("oi")
    acoes = ["andar", "coletar", "retornar"]
    percepcoes = ["ver"]
    localizacao = [0,0]
    agenteSimplesInstance = AgenteGenerico.AgenteGenerico(acoes=acoes, percepcoes=percepcoes, localizacao=localizacao)
    print("Testando POO", )
