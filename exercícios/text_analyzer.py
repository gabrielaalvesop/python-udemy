text=input("Digite o texto a ser analisado: ")

def text_analyzer(text):
    number_of_characters = len(text)
    number_of_words = len(text.split())
    number_of_sentences = text.count('.') + text.count('!') + text.count('?')

    return {
        'Número de caracteres': number_of_characters,
        'Número de palavras': number_of_words,
        'Número de frases': number_of_sentences
    }


result = text_analyzer(text)

for key, value in result.items():
    print(f"{key}: {value}")
    