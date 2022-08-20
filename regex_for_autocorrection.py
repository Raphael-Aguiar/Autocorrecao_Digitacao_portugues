# Esse programa pega um arquivo de texto com palavras acentuadas e as coloca
# na forma de código para que a linguagem AutoHotKey possa acentuar
# automaticamente as palavras em português não acentuadas.
# As seguintes páginas do dicionário dicio.com foram usadas para compilar o
# arquivo txt:
# https://www.dicio.com.br/palavras-com-acento-agudo-no-a/
# https://www.dicio.com.br/palavras-com-c-cedilha/
# https://www.dicio.com.br/palavras-com-acento-circunflexo/
# https://www.dicio.com.br/palavras-com-ao/
# https://www.dicio.com.br/palavras-com-acento-agudo/
# https://www.dicio.com.br/palavras-acento/
# Exemplo: no arquivo de saída, em vez da palavra "êxito", haverá uma linha
# assim: "::exito::êxito"
# Consulte o site do AutoHotKey (https://www.autohotkey.com/) para mais
# informações

import re

lista_acentuada = []
lista_sem_acento = []
codigo_final = []

# Cria uma lista com todas as palavras acentuadas
# OBS: mude o nome do path e do arquivo para os de sua preferência
with open('D:\OneDrive\Scripts\projects\dicionario_ahk\Dicionário_Final.txt'
        , "r",
          encoding="utf-8") as texto:
    for linha in texto:
        strip_line = linha.strip()
        m = lista_acentuada.append(strip_line)

# Tranforma a lista em conjunto, e novamente em lista, para eliminar
# palavras duplicadas
lista_acentuada = set(lista_acentuada)
lista_acentuada = list(lista_acentuada)
lista_acentuada.sort(key=str.lower)

# Usa a função re.sub() para tirar todos os acentos e compilar uma segunda
# lista, de palavras não acentuadas
for palavra in lista_acentuada:
    palavra_sem_acento = re.sub('[áâã]', 'a', palavra)
    palavra_sem_acento = re.sub('[éê]', 'e', palavra_sem_acento)
    palavra_sem_acento = re.sub('í', 'i', palavra_sem_acento)
    palavra_sem_acento = re.sub('[óõô]', 'o', palavra_sem_acento)
    palavra_sem_acento = re.sub('ú', 'u', palavra_sem_acento)
    palavra_sem_acento = palavra_sem_acento.strip()
    n = lista_sem_acento.append(palavra_sem_acento)

# Faz o "match" entre as palavras com e sem acento de cada uma das listas no
# formato de "hotstrings" (::cafe::café) da linguagem AutoHotKey:
count = 0
while count < len(lista_acentuada):
    linha_final = str("::" + str(lista_sem_acento[count]) + "::" +
                      str(lista_acentuada[count]))
    f = codigo_final.append(linha_final)
    count += 1

# Tira da lista palavras com apenas uma ou duas letras
codigo_final = [x for x in codigo_final if not re.search(r'::.::', x)]
codigo_final = [x for x in codigo_final if not re.search(r'::..::', x)]

# Grava o orquivo final
with open("D:\OneDrive\Scripts\projects\dicionario_ahk\Lista_final.txt",
          'w') as file:
    for item in codigo_final:
        file.write("%s\n" % item)

print("arquivo Lista_final.txt compilado com êxito!")
