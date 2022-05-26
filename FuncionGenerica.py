class FuncionGenerica:
    lista = {'uno', 'dos', 'tres', 'cuatro'}
    c = []

    for elem in lista:
        print(elem)
        c.append(elem)

    print(c)

    #No es necesario utilizar una Collection en Python ya que las listas de por si aceptan cualquier tipo de dato.
    @staticmethod
    def print (c):
        for elem in c:
            print(f'{elem}')
        print(f'------------------------------')
