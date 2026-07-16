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

#titulo do jogo
print("Jogo da Forca\n") 

palavra_secreta, letras_acertadas = inicializar_jogo()
chances = 6 

while True:
    palavra_oculta = ""

for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_oculta += letra + " "  # Mostra a letra se já foi acertada
        else:
            palavra_oculta += "_ "    
        
print(f"\nPalavra atual: {palavra_oculta}")
    print(f"Chances restantes: {chances}")        

  if "_" not in palavra_oculta:
        print("Parabéns! Você descobriu a palavra por completo!")
        break     