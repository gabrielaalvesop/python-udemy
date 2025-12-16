import copy

import produtos_modulo as pm

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(pm.produtos_desordenados)
]

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(pm.produtos_desordenados),
    key=lambda p: p['nome'],
    reverse=True
)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(pm.produtos_desordenados),
    key=lambda p: p['preco']
)

print(*pm.produtos_desordenados, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
