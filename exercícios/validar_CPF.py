import sys

cpf_enviado_pelo_usuario = input("Digite o CPF: ").replace(".", "").replace("-", "")

entrada_sequencial_igual = cpf_enviado_pelo_usuario == cpf_enviado_pelo_usuario[0] * len(cpf_enviado_pelo_usuario)

if entrada_sequencial_igual:
    print("Você enviou dados sequenciais iguais.")
    sys.exit()

nove_digitos = cpf_enviado_pelo_usuario[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0


for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1=(resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print("O primeiro dígito verificador é:", digito_1)

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print("O segundo dígito verificador é:", digito_2)

cpf_gerado = nove_digitos + str(digito_1) + str(digito_2)
print("O CPF gerado é:", cpf_gerado)

if cpf_gerado == cpf_enviado_pelo_usuario:
    print("CPF válido")
else:
    print("CPF inválido")
    