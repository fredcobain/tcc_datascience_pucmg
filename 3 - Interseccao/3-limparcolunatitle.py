## Esse código é pra remover os caracteres " e : dos CSVs

import re

with open('android_titles_2.csv', 'r',encoding='utf-8') as file_android:
    csv_android = file_android.read()

with open('ios_titles_2.csv', 'r',encoding='utf-8') as file_ios:
    csv_ios = file_ios.read()

#Definindo que queremos eliminar os caracteres do tipo " e : para não bagunçar a geração do csv
str_colon = ':'
str_quote = "'"
str_dbquote = '"'
replace_str = ''

# Eliminando o caractere " e : nos 2 arquivos
new_csv_android = re.sub(str_dbquote, replace_str, csv_android)
new_csv_android = re.sub(str_colon, replace_str, csv_android)
new_csv_ios = re.sub(str_dbquote, replace_str, csv_ios)
new_csv_ios = re.sub(str_colon, replace_str, csv_ios)

# Definindo o nome dos novos arquivos 
new_csv_android_path = 'android_titles_limpo.csv'
new_csv_ios_path = 'ios_titles_limpo.csv'

#Gerando novos arquivos
with open(new_csv_android_path, 'w',encoding='utf-8') as new_file_android:
    new_file_android.write(new_csv_android)

with open(new_csv_ios_path, 'w',encoding='utf-8') as new_file_ios:
    new_file_ios.write(new_csv_ios)

#FIM DA SEGUNDA LIMPEZA




