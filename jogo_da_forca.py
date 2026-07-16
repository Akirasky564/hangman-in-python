# Lista de palavras que serão usadas para o sorteio do jogo
lista_palavras = ["python", "programacao", "desenvolvimento", "jogo", "forca"]

def inicializar_jogo():

# Sorteia uma palavra aleatória da lista 
palavra = random.choice(lista_palavras)

# Cria um conjunto vazio (set) para armazenar as letras acertadas pelo jogador
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
            palavra_oculta += "_ " # Mostra um traço se ainda não foi descoberta

  # Exibe o status atual do jogo para o jogador        
print(f"\nPalavra atual: {palavra_oculta}")
print(f"Chances restantes: {chances}")    

  # VERIFICAÇÃO DE VITÓRIA
  if "_" not in palavra_oculta:
        print("Parabéns! Você descobriu a palavra por completo!")
        break     

chute = input("Digite uma letra ou chute a palavra: ").upper().strip()

if len(chute) > 1:
        if chute == palavra_secreta:
            print(
                f"\nSensacional! Você acertou a palavra inteira: {palavra_secreta}"
            )
            break  # Vitória instantânea: encerra o jogo
        else:
            print(f"Ops! O chute '{chute}' está incorreto.")
            chances -= 1  # Penalidade por errar o chute da palavra

elif len(chute) == 1:
        # PROCESSAMENTO DA JOGADA
        acertou = processar_tentativa(
            chute, palavra_secreta, letras_acertadas
        )
        # Exibe o feedback e aplica a penalidade em caso de erro
        if acertou:
            print("Parabéns! Você acertou a letra.")
        else:
            print("Ops! A letra digitada não faz parte da palavra.")
            chances -= 1  # Deduz uma chance do jogador
        else:
        print("Você não digitou nada. Tente novamente.")
        continue 

# VERIFICAÇÃO DE DERROTA
if chances == 0:
        print(
            f"\nGame Over! Suas chances acabaram. A palavra era: {palavra_secreta}"
        )
        break         