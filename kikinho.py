from mendeleev import element # Importa bibliotecas necessárias (mendeleev e random)
import random

elementosPossíveis = set(range(1,119)) # Um conjunto com todos os 118 elementos, por número atômico

perguntasPossíveis = { # Um conjunto com todas as perguntas não específicas possíveis
    "O seu elemento é um metal de transição?",
    "O seu elemento faz ligação covalente?",
    "O seu elemento tem 8 elétrons na camada de valência?",
    "O seu elemento é da família do Boro?",
    "O seu elemento é da família do Carbono?",
    "O seu elemento é da família do Nitrogênio?",
    "O seu elemento é da família dos halogênios?",
    "O seu elemento é da família dos calcogênios?",
    "É possível saber o estado físico do seu elemento em 25°C?",
    "Em condições normais de pressão e temperatura, seu elemento é um gás?",
    "Em condições normais de pressão e temperatura, seu elemento é um líquido?",
    "Em condições normais de pressão e temperatura, seu elemento é um sólido?",
    "O seu elemento é radioativo?",
    "O seu elemento é um bom condutor térmico?(acima de 8 W/mK)",
    "O seu elemento é sintético?",
    "O seu elemento é utilizado na fabricação de smartphones?",
    "O seu elemento lembra o nome de um cientista?",
    "O seu elemento lembra o nome de um planeta?",
    "O seu elemento lembra o nome de um lugar (país, cidade, estado, província)?",
    "O seu elemento está presente na composição do sal de cozinha?",
    "O seu elemento é utilizado na composição de pilhas e baterias?",
    "O seu elemento é utilizado na fabricação de joias?",
}

perguntas = { # Um dicionário com as perguntas gerais e os seus elementos correspondentes
    "O seu elemento é um metal de transição?": {21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 39, 40, 41, 42, 43, 44, 45, 46, 48, 57, 72, 73, 74, 75, 76, 77, 78, 80, 89, 104, 105, 106, 107, 108, 109, 110, 112},
    "O seu elemento faz ligação covalente?":{1, 2, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 31, 32, 33, 34, 35, 36, 47, 49, 50, 51, 52, 53, 54, 79, 81, 82, 83, 84, 85, 86, 111, 113, 114, 115, 116, 117, 118},
    "O seu elemento tem 8 elétrons na camada de valência?":{36, 10, 18, 54, 86, 118},
    "O seu elemento é da família do Boro?":{5, 13, 81, 49, 113, 31},
    "O seu elemento é da família do Carbono?":{32, 6, 14, 50, 82, 114},
    "O seu elemento é da família do Nitrogênio?":{33, 83, 51, 115, 7, 15},
    "O seu elemento é da família dos halogênios?":{35, 9, 17, 85, 53, 117},
    "O seu elemento é da família dos calcogênios?":{34, 8, 16, 52, 84, 116},
    "É possível saber o estado físico do seu elemento em 25°C?":{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 102, 103},
    "Em condições normais de pressão e temperatura, seu elemento é um gás?": {1, 2, 36, 7, 8, 9, 10, 17, 18, 54, 86}, 
    "Em condições normais de pressão e temperatura, seu elemento é um líquido?":{80, 35}, 
    "Em condições normais de pressão e temperatura, seu elemento é um sólido?":{3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59,60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82, 83, 84, 85, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 100, 101, 102},
    "O seu elemento é radioativo?":{43, 61, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118}, 
    "O seu elemento é um bom condutor térmico?(acima de 8 W/mK)":{3, 4, 5, 11, 12, 13, 14, 19, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 37, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 55, 57, 58, 59, 61, 63, 65, 66, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 92}, 
    "O seu elemento é sintético?":{95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118}, 
    "O seu elemento é utilizado na fabricação de smartphones?":{19, 31, 33, 42, 47, 50, 79},
    "O seu elemento lembra o nome de um cientista?":{99, 114, 100, 64, 112, 104, 107, 96, 103, 101, 109, 102, 118, 111, 106},
    "O seu elemento lembra o nome de um planeta?":{80, 92, 93, 94},
    "O seu elemento lembra o nome de um lugar (país, cidade, estado, província)?":{21, 49, 84, 95, 98, 87, 32, 115, 110, 105, 63},
    "O seu elemento está presente na composição do sal de cozinha?":{11,17},
    "O seu elemento é utilizado na composição de pilhas e baterias?":{3,41},
    "O seu elemento é utilizado na fabricação de joias?":{6, 46, 47, 78, 79},
}

perguntasEspecíficas = { # Um dicionário com as perguntas específicas e seu único elemento correspondente
    "O modelo de Bohr é válido para o seu elemento?":{1},
    "O seu elemento é o predominante na composição do Sol?":{2},
    "O seu elemento é utilizado na composição de pilhas e baterias?":{3},
    "É famoso por ser utilizado na composição de creme dental?":{9},
    "O seu elemento é encontrado na clorofila?":{12},
    "O seu elemento é utilizado na limpeza de piscinas?":{17},
    "O seu elemento pode ajudar a evitar pedra nos rins?":{19},
    "O seu elemento é essencial para a manutenção dos ossos?":{20},
    "O seu elemento auxilia no trasporte do Oxigênio pelo corpos animais?":{26},
    "O seu elemento é utilizado para fazer fios elétricos?":{29},
    "O seu elemento se parece com o nome do planeta do Super-Homem?":{36},
    "O seu elemento é utilizado para desinfetar machucados?":{53},
    "O seu elemento possui um isótopo radioativo responsável pelo acidente em Goiânia de 1987?":{55},
    "O seu elemento era usado em termômetros?":{80},
}

print("Olá, sou o Kikinho, gênio da tabela periódica da Ilum Escola de Ciência.")

perguntaAtual = "O seu elemento faz ligação covalente?" # Define a primeira pergunta como a pergunta atual

while perguntasPossíveis != set(): # Enquanto ainda houver perguntas possíveis:

    listaExcluída = set() # Limpa a lista de elementos a serem excluídos a cada iteração (usada posteriormente)
    resposta = "" # Limpa a variável que contém a resposta para a pergunta atual
    resposta = input(perguntaAtual+"\n") # Uma variável que contém a resposta para a pergunta atual

    if resposta == "s": # Se a resposta for sim:
        for elemento in elementosPossíveis: # Para cada elemento possível,
            if elemento not in perguntas[perguntaAtual]: # Se este elemento não corresponde à pergunta:
                listaExcluída.add(elemento) # Adiciona o elemento à lista para exclusão
    
    elementosPossíveis = elementosPossíveis - listaExcluída # Retira a lista de exclusão da lista de elementos possíveis
    
    if resposta == "n": # Se a resposta for não:
        elementosPossíveis = elementosPossíveis - perguntas[perguntaAtual] # Retira os elementos correspondentes à pergunta da lista de elementos possíveis

    # print(elementosPossíveis) -------------------------------------------- IGNORAR (Usado para debugging)
    
    perguntasPossíveis.remove(perguntaAtual) # Remove a pergunta atual da lista de perguntas possíveis, impedindo que as perguntas se repitam

    for chave in perguntas: # Para cada pergunta no dicionário perguntas:
        if elementosPossíveis.intersection(perguntas[chave]) == set() and chave in perguntasPossíveis: # Se não houver nenhuma pergunta em comum com elementos possíveis:
            perguntasPossíveis.remove(chave) # Remove pergunta de perguntas possíveis
    
    if perguntasPossíveis == set(): # Se não houver mais perguntas possíveis:
        
    #print("a") ------------------------------------------------------------ IGNORAR (Usado para debugging)
    
        for chave, valor in perguntasEspecíficas.items(): # Para cada par chave-valor no dicionário de perguntas específicas:
            if list(valor)[0] in elementosPossíveis: # Se o elemento correspondente (valor) estiver entre os elementos possíveis:
                perguntas[chave] = valor # Adiciona o par chave-valor (pergunta e elemento) ao dicionário de perguntas normais
                perguntasPossíveis.add(chave) # Adiciona a pergunta (chave) à lista de perguntas possíveis

    listaTemporária = list(perguntasPossíveis) # Uma lista temporária que é uma cópia do conjunto de perguntas possíveis
    
    if listaTemporária != [] and len(elementosPossíveis) >= 2: # Se houver alguma pergunta na lista temporária e ainda houver algum elemento possível:
        perguntaAtual = random.choice(listaTemporária) # Define uma pergunta aleatória das restantes como pergunta atual
   
    if len(elementosPossíveis) <= 2: # Se houver apenas 2 ou menos elementos:
        break # Sai do loop while, para adivinhar seu elemento

resultadoTemporário = list(elementosPossíveis) # Cria uma lista para o resultado temporário

for número in range(len(resultadoTemporário)): # Por um número N de vezes que é igual ao tamanho da lista temporária (número de elementos possíveis):
    elementoAdivinhado = resultadoTemporário[número] # Define o valor com index de número N da lista como o elemento a ser adivinhado
    respostaFinal = input("O seu elemento é o "+element(resultadoTemporário[número]).name+"?\n") # Uma variável que contém a resposta se este é o elemento certo
    # Note acima o uso da biblioteca mendeleev para obtenção do nome do elemento a partir de seu número atômico! :)
    
    if respostaFinal == 's': # Se a resposta final for sim:
        print("Isso! Consegui acertar! De primeira hein? ;)") # :D
        break # Sai do loop for, para parar de chutar outros elementos
    elif número == len(resultadoTemporário)-1 and respostaFinal == 'n': # Senão, se for o último elemento da lista e a resposta final for não:
        print("Baixo astral, cara. Não consegui adivinhar o seu elemento. Você me venceu. :'(") # :(
