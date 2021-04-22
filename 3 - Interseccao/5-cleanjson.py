## Esse código é pra transformar os caracteres ' em " do Arquivo JSON

import re

with open('result_titles.json', 'r',encoding='utf-8') as file_result:
    json_result = file_result.read()


#Definindo que queremos substituir os caracteres do tipo ' por "
str_quote = "'"
str_dbquote = '"'


# Substituindo o caractere ' por "
new_json_result = re.sub(str_quote, str_dbquote, json_result)


# Definindo o nome dos novos arquivos 
new_json_path = 'result_titles_limpo.json'


#Gerando novos arquivos
with open(new_json_path, 'w',encoding='utf-8') as new_file_result:
    new_file_result.write(new_json_result)


#FIM DA TERCEIRA LIMPEZA






