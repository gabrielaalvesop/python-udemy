def mutiplicar(a,b,*args):
    resultado = a * b
    for numero in args:
        resultado *= numero
    return resultado

conta=mutiplicar(2,3,4,5,10)
print(conta)

