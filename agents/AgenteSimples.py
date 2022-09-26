import agents.AgenteGenerico as AgenteGenerico

acoes = []
percepcoes = []
localizacao = []

AgenteGenerico = AgenteGenerico.AgenteGenerico(acoes, percepcoes, localizacao)

class AgenteSimples(AgenteGenerico):
    def __init__(self):
        super().__init__(acoes, percepcoes, localizacao)
