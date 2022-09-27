from agents.AgenteGenerico import AgenteGenerico

acoes = []
percepcoes = []
localizacao = []

# AgenteGenerico = AgenteGenerico.AgenteGenerico(acoes, percepcoes, localizacao)

class AgenteSimples(AgenteGenerico):
    def __init__(self, acoes, percepcoes, localizacao):
        # super().__init__()
        self.acoes = acoes
        self. percepcoes = percepcoes
        self.localizacao = localizacao
        # print(self)

# class AgenteSimples(AgenteGenerico):
#     def __init__(self):
#         super().__init__(acoes, percepcoes, localizacao)
#         print(self)
