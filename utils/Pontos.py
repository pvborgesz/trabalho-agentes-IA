from random import randint

import numpy as np

def geradorPontos():
    Pontos = []
    while len(Pontos) < 10:
        random_c = randint(0, 20)
        random_l = randint(0, 20)
        if (random_c, random_l) not in Pontos:
            Pontos.append((random_c, random_l))
    # print(Pontos)
    return Pontos

# geradorPontos()

# bem simples ainda, só um gerador de coordenada entre 0 e 20, vai precisar de alteração