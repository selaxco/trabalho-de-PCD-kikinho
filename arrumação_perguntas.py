""" Esse código foi utilizado para 'classificar', por meio da biblioteca mendeleev, os elementos para poder atribuí-los às perguntas feitas.
As perguntas que não constam aqui tiveram seus elementos transcritos à mão, com informações provenientes de perquisas. """

# Perguntas sobre famílias (o código é igual para todas as famílias):

for elemento in elementosPossíveis: # Para cada elemento na lista completa de elementos:
    if  element(elemento).group != None and element(elemento).group.name == "Boron group": # Se o elemento tiver uma família atribuída na biblioteca e esta for
                                                                                           # a família do Boro:
        if perguntas["O seu elemento é da família do Boro?"]!={}:
            perguntas["O seu elemento é da família do Boro?"].add(elemento) # Adiciona o elemento como valor da pergunta sobre família do Boro no dicionário de
                                                                            # perguntas
        else:
            perguntas["O seu elemento é da família do Boro?"]=(elemento)

for elemento in elementosPossíveis: 
    if  element(elemento).group != None and element(elemento).group.name == "Carbon group":
        if perguntas["O seu elemento é da família do Carbono?"]!={}:
            perguntas["O seu elemento é da família do Carbono?"].add(elemento)
        else:
            perguntas["O seu elemento é da família do Carbono?"]=(elemento)

for elemento in elementosPossíveis:
    if element(elemento).group != None and element(elemento).group.name == "Pnictogens":
        if perguntas["O seu elemento é da família do Nitrogênio?"]!={}:
            perguntas["O seu elemento é da família do Nitrogênio?"].add(elemento)
        else:
            perguntas["O seu elemento é da família do Nitrogênio?"]=(elemento)

for elemento in elementosPossíveis:
    if  element(elemento).group != None and element(elemento).group.name == "Noble gases" and elemento != 2: # O elemento deve ser diferente do Hélio pois este é
                                                                                                             # um gás nobre porém não possui 8 elétron na camada de
                                                                                                             # valência
        if perguntas["O seu elemento tem 8 elétrons na camada de valência?"]!={}:
            perguntas["O seu elemento tem 8 elétrons na camada de valência?"].add(elemento)
        else:
            perguntas["O seu elemento tem 8 elétrons na camada de valência?"]=(elemento)

for elemento in elementosPossíveis:
    if  element(elemento).group != None and element(elemento).group.name == "Halogens":
        if perguntas["O seu elemento é da família dos halogênios?"]!={}:
            perguntas["O seu elemento é da família dos halogênios?"].add(elemento)
        else:
            perguntas["O seu elemento é da família dos halogênios?"]=(elemento)

for elemento in elementosPossíveis:
    if  element(elemento).group != None and element(elemento).group.name == "Chalcogens":
        if perguntas["O seu elemento é da família dos calcogênios?"]!={}:
            perguntas["O seu elemento é da família dos calcogênios?"].add(elemento)
        else:
            perguntas["O seu elemento é da família dos calcogênios?"]=(elemento)

for elemento in elementosPossíveis:
    if  element(elemento).group != None and element(elemento).group.name == "":
        if perguntas["O seu elemento é um metal de transição?"]!={}:
            perguntas["O seu elemento é um metal de transição?"].add(elemento)
        else:
            perguntas["O seu elemento é um metal de transição?"]=(elemento)

for elemento in elementosPossíveis: 
    if  element(elemento).is_radioactive == True:
        if perguntas["O seu elemento é radioativo?"]!={}:
            perguntas["O seu elemento é radioativo?"].add(elemento)
        else:
            perguntas["O seu elemento é radioativo?"]=(elemento)

for elemento in elementosPossíveis:
    if  element(elemento).group != None and element(elemento).group.name != "" and element(elemento).group.name != "Alkaline earths" and element(elemento).group.name != "Alkali metals":
        if perguntas["O seu elemento faz ligação covalente?"]!={}:
            perguntas["O seu elemento faz ligação covalente?"].add(elemento)
        else:
            perguntas["O seu elemento faz ligação covalente?"]=(elemento)

for elemento in elementosPossíveis:
    if  element(elemento).thermal_conductivity != None and element(elemento).thermal_conductivity >= 8:
        if perguntas["O seu elemento é um bom condutor térmico?(acima de 8 W/mK)"]!={}:
            perguntas["O seu elemento é um bom condutor térmico?(acima de 8 W/mK)"].add(elemento)
        else:
            perguntas["O seu elemento é um bom condutor térmico?(acima de 8 W/mK)"]=(elemento)

for elemento in elementosPossíveis:
    if element(elemento).melting_point != None and element(elemento).melting_point >= 298:
        if perguntas["Em condições normais de pressão e temperatura, seu elemento é um sólido?"]!={}:
            perguntas["Em condições normais de pressão e temperatura, seu elemento é um sólido?"].add(elemento)
        else:
            perguntas["Em condições normais de pressão e temperatura, seu elemento é um sólido?"] = elemento

for elemento in elementosPossíveis:
    if element(elemento).melting_point != None and element(elemento).melting_point < 298 and element(elemento).boiling_point != None and element(elemento).boiling_point > 298:
        if perguntas["Em condições normais de pressão e temperatura, seu elemento é um líquido?"]!={}:
            perguntas["Em condições normais de pressão e temperatura, seu elemento é um líquido?"].add(elemento)
        else:
            perguntas["Em condições normais de pressão e temperatura, seu elemento é um líquido?"] = elemento

for elemento in elementosPossíveis:
    if element(elemento).boiling_point != None and element(elemento).boiling_point <= 298:
        if perguntas["Em condições normais de pressão e temperatura, seu elemento é um gás?"]!={}:
            perguntas["Em condições normais de pressão e temperatura, seu elemento é um gás?"].add(elemento)
        else:
            perguntas["Em condições normais de pressão e temperatura, seu elemento é um gás?"] = elemento
