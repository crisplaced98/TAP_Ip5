from Cosa2 import Cosa2
from Gato import Gato
from Animal import Animal

class UsaCosa2:
    g = Gato(1, 2)
    c = Cosa2(g)
    c.nombre = g

    g2 = c.nombre
    a = c.nombre
    print(g2.habla())
    print(a.habla())

    #En Java esto es ilegal. En Python no.
    c = Cosa2('www')
    print(c.nombre)

