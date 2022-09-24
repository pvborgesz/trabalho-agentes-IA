import agents.AgenteGenerico as AgenteGenerico

# AgenteGenerico = agents.AgenteGenerico.AgenteGenerico(acoes, percepcoes, localizacao)

class AgenteSimples(AgenteGenerico.AgenteGenerico(acoes="", percepcoes="", localizacao="")):
    def __init__(self):
        super().__init__(acoes, percepcoes, localizacao)
