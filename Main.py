import agents.AgenteSimples as AgenteSimples


class Main:
    # def __init__(self,val):
    print("oi")
    acoes = ["andar", "coletar", "retornar"]
    percepcoes = ["ver"]
    localizacao = [0,0]
    agenteSimplesInstance = AgenteSimples.AgenteSimples(acoes=acoes, percepcoes=percepcoes, localizacao=localizacao)
    print("Testando POO", )
