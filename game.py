from random import choice
from colorama import Fore

categorias = {}

with open('palavras.txt', 'r') as file:
  conteudo = file.read()
exec(conteudo)

# Adiciona as listas ao dicionário de categorias
categorias['fruta'] = fruta
categorias['país'] = país
categorias['animal'] = animal
categorias['profissao'] = profissao
categorias['cor'] = cor

#Listas de diferentes categorias contendo as palavras

# Definiçã da função, além do título e decoração para a interface do jogo
def jogodaforca():
  print(Fore.LIGHTGREEN_EX + "=-="*10)
  print(Fore.LIGHTYELLOW_EX + 'Jogo da Forca'.center(30))
  print(Fore.LIGHTGREEN_EX + "=-="*10, Fore.RESET)
  
  # Escolha aleatória da categoria e da palavra dentro da categoria
  categoria = ["animal", "país", "fruta", "profissao", "cor"]
  escolha_categoria = choice(categoria)
  palavra_sorteada = ''
  if escolha_categoria == "animal":
    palavra_sorteada = str(choice(animal)).lower()
  elif escolha_categoria == "país":
    palavra_sorteada = str(choice(país)).lower()
  elif escolha_categoria == "fruta":
    palavra_sorteada = str(choice(fruta)).lower()
  elif escolha_categoria == "cor":
    palavra_sorteada = str(choice(cor)).lower()
  elif escolha_categoria == "profissao":
    palavra_sorteada = str(choice(profissao)).lower()
    
  # A palavra sorteada é transformada em underlines para ocultar suas letras
  palavra_secreta = str(len(palavra_sorteada)*"_")

  # Caso a palavra sorteada tenha espaço, será transformado em hífen
  if ' ' in palavra_sorteada:
    for s in range(len(palavra_sorteada)):
      if palavra_sorteada[s] == ' ':
        palavra_secreta = (palavra_secreta[:s] + '-' + palavra_secreta[s+1:])
        palavra_sorteada = (palavra_sorteada[:s] + '-' + palavra_sorteada[s+1:])

  # Definição do loop, de acordo com o número de tentativas 
  tentativas = 6
  fim_jogo = 0
  letras_digitadas = []
  # Formatação da interface de acordo com a categoria escolhida, junto com o desenho inicial da forca
  if escolha_categoria == ('frutas', 'profissao', 'cor'):
    print(f'\nA palavra é uma {Fore.LIGHTYELLOW_EX}{escolha_categoria}{Fore.RESET}, '
          f'tente adivinhar! ')
  else: 
    print(f'\nA palavra é um {Fore.LIGHTYELLOW_EX}{escolha_categoria}{Fore.RESET}, '
      f'tente adivinhar! ')
    print(f'{Fore.LIGHTRED_EX}Você tem {tentativas} tentativas {Fore.RESET}\n')
    print('''                --------------           
                |            |
                |            
                |           
                |            
                |           
                |_______________''')
    
    # Definição do loop de tentativas e entrada do palpite
    while tentativas > 0:
      for _ in range(tentativas):
        print(f'{palavra_secreta}\n')
        palpite = str(input('Digite uma letra ou a resposta: ')).lower()
      
        # Se o jogador digitar um caractere que não seja uma letra ou hífen, será alertado pelo programa
        if palpite.isalpha() is False and "-" not in palpite:
          print(f'{Fore.LIGHTRED_EX}Você deve digitar uma letra!{Fore.RESET}\n')
          tentativas -= 0
          
        # Se a letra digitada estiver na palavra, os underlines serão substituídos pela letra nas posições correspondentes
        if palpite in palavra_sorteada:
          tentativas -= 0
          for i in range(len(palavra_sorteada)):
            if palavra_sorteada[i] == palpite:
              palavra_secreta = (palavra_secreta[:i] + palpite + palavra_secreta[i+1:])
  
             # Se a letra digitada não estiver na palavra, o programa alertará e o jogador perderá uma tentativa
        if palpite not in palavra_sorteada:
          if palpite not in letras_digitadas:
            if palpite.isalpha() is True:
              if len(palpite) == 1:
                print(f'\n{Fore.RED}A palavra não tem a letra {palpite.capitalize()}! '
                f'{Fore.RESET}\n')
                tentativas -= 1
                if tentativas >= 1:
                  print(f'{Fore.LIGHTRED_EX}Você tem {tentativas} tentativas {Fore.RESET}\n')
    
             # Em caso de repetição da letra pelo jogador, o programa emitirá um aviso.
        if palpite in letras_digitadas:
          print(f'{Fore.LIGHTRED_EX}Você já tentou a letra {palpite}!{Fore.RESET}\n')
          tentativas -= 0
        else:
          letras_digitadas.append((palpite))  
  
        # Se a tentativa do jogador ao responder ter um número de caracteres menor que a resposta correta, o programa emitirá um alerta ao jogador.
        if len(palpite) != 1 and len(palpite)<len(palavra_sorteada):
          tentativas -= 0
          print(f'{Fore.LIGHTRED_EX}\nA palavra tem {len(palavra_secreta)} '
                f'letras, digite uma letra ou tente acertar a palavra!\n{Fore.RESET}')

        # Se o jogador completar todas as letras, o jogo termina
        if palavra_secreta.isalpha() is True:
          print(f'Parabéns, você acertou! A palavra era {Fore.LIGHTGREEN_EX}{palavra_sorteada}{Fore.RESET}')
          fim_jogo = 1
          
        # Se o jogador decidir tentar chutar a palavra e acertar, o jogo terminará
        if palpite == palavra_sorteada:
          print(f'Você acertou! A palavra era {Fore.LIGHTGREEN_EX}{palavra_sorteada} '
                f'{Fore.RESET}')
          fim_jogo = 1
          
        # Se o jogador decidir tentar chutar a palavra e errar, o jogo terminará
        if palpite != palavra_sorteada:
         if len(palpite) == len(palavra_secreta) or len(palpite) >= int(0.8*len
         (palavra_sorteada)):
            print(f'Você perdeu! A palavra era {palavra_sorteada}')
            fim_jogo = 1
           
        # desenha a forca de acordo com o restante de tentativas
        if tentativas == 5:
                  print(f'''                --------------      {letras_digitadas} 
                |            |
                |            {Fore.LIGHTBLUE_EX}O{Fore.RESET}
                |           
                |            
                |           
                |_______________''')

        if tentativas == 4:
            print(f'''                --------------      {letras_digitadas} 
                |            |
                |            {Fore.LIGHTBLUE_EX}O{Fore.RESET}
                |            {Fore.LIGHTBLUE_EX}|{Fore.RESET}
                |            {Fore.LIGHTBLUE_EX}|{Fore.RESET}
                |           
                |_______________''')
        
        if tentativas == 3:
          print(f'''                --------------      {letras_digitadas}
                |            |
                |            {Fore.LIGHTBLUE_EX}O{Fore.RESET}
                |            {Fore.LIGHTBLUE_EX}|\\{Fore.RESET}
                |            {Fore.LIGHTBLUE_EX}|{Fore.RESET}
                |          
                |_______________''')

        if tentativas == 2:
          print(f'''                --------------      {letras_digitadas}
                |            |
                |            {Fore.LIGHTBLUE_EX}O{Fore.RESET}
                |           {Fore.LIGHTBLUE_EX}/|\\{Fore.RESET}
                |            {Fore.LIGHTBLUE_EX}|{Fore.RESET}
                |           
                |_______________''')

        if tentativas == 1:
          print(f'''                --------------      {letras_digitadas}
                |            |
                |            {Fore.LIGHTRED_EX}O{Fore.RESET}
                |           {Fore.LIGHTRED_EX}/|\\{Fore.RESET}
                |            {Fore.LIGHTRED_EX}|{Fore.RESET}
                |           {Fore.LIGHTRED_EX}/ {Fore.RESET}
                |_______________''')

        if tentativas == 0:
          print(f'''                --------------      {letras_digitadas}
                |            |
                |            {Fore.RED}O{Fore.RESET}
                |           {Fore.RED}/|\\{Fore.RESET}
                |            {Fore.RED}|{Fore.RESET}
                |           {Fore.RED}/ \\{Fore.RESET}
                |_______________''')

        # Implementa um loop que oferece ao usuário a opção de jogar novamente ou encerrar o programa
        if tentativas == 0:
          print(f'\n{Fore.RED}Acabaram suas tentativas, você perdeu\n'
                            f'A palavra era {Fore.LIGHTGREEN_EX}{palavra_sorteada}!{Fore.RESET}\n')
        if fim_jogo == 1 or tentativas == 0:
          while True:
            retornar = input(f'Quer jogar outra vez?\n\n'
            f'{Fore.LIGHTGREEN_EX}[1] Sim \n{Fore.RESET}'
            f'{Fore.RED}[2] Não \n{Fore.RESET}')
            if retornar == '1':
              jogodaforca()
            elif retornar == '2':
              print('Até a próxima!')
              break
            else:
              print('Resposta inválida')
              continue
    
jogodaforca()
  
