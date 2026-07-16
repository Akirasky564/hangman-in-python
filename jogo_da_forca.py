lista_palavras = ["python", "programacao", "desenvolvimento", "jogo", "forca"]

def inicializar_jogo():
palavra = random.choice(lista_palavras)
tentativas_set = set() 
return palavra, tentativas_set

def processar_tentativa(letra, palavra_secreta, letras_acertadas):
    if letra in palavra_secreta:
        letras_acertadas.add(letra)
        return True
    else:
        return False

'''titulo do jogo'''
print("Jogo da Forca\n") 

palavra_secreta, letras_acertadas = inicializar_jogo()
chances = 6 

while True:
    palavra_oculta = ""