def criar_mutiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

dobro = criar_mutiplicador(2)
triplo = criar_mutiplicador(3)
quadruplo = criar_mutiplicador(4)

print(dobro(5))
print(triplo(5))
print(quadruplo(5)) 
