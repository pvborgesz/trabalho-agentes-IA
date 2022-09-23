class AgenteGenerico:
  def __init__(self, acoes, percepcoes, localizacao): ##constructor da classe
    self.acoes = acoes ## tipo list
    self.percepcoes = percepcoes ## 
    self.localizacao = localizacao ## 

  def getAcoes(self):
    print(self.acoes)
    