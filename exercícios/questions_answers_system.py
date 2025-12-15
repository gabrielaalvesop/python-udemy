print("=== Sistema de Perguntas e Respostas ===")

questions = [
    "Quanto é 2 + 2? ",
    "Qual é a capital da França? ",
    "Qual é a cor do céu em um dia claro? "
]

answers = [
    "4",
    "Paris",
    "azul"
]

score = 0

for i in range(len(questions)):
    user_answer = input(questions[i])
    if user_answer.strip().lower() == answers[i].strip().lower():
        print("Resposta correta!")
        score += 1
    else:
        print(f"Resposta incorreta! A resposta correta é: {answers[i]}")
    print()
print(f"Sua pontuação final é: {score} de {len(questions)}")
