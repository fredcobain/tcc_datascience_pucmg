## Esse código é pra remover os caracteres ' dos CSVs

import re

with open('android_apps_br_paid.csv', 'r',encoding='utf-8') as file_android:
    csv_android = file_android.read()

with open('ios_apps_br_paid.csv', 'r',encoding='utf-8') as file_ios:
    csv_ios = file_ios.read()

#Definindo que queremos eliminar os caracteres do tipo ' para não bagunçar a geração do JSON
str_quote = "'"
#str_dbquote = '"'
replace_str = ''

# Eliminando o caractere ' nos 2 arquivos
new_csv_android = re.sub(str_quote, replace_str, csv_android)
new_csv_ios = re.sub(str_quote, replace_str, csv_ios)

# Definindo o nome dos novos arquivos 
new_csv_android_path = 'android_apps_br_limpo.csv' # or whatever path and name you want
new_csv_ios_path = 'ios_apps_br_limpo.csv' # or whatever path and name you want

#Gerando novos arquivos
with open(new_csv_android_path, 'w',encoding='utf-8') as new_file_android:
    new_file_android.write(new_csv_android)

with open(new_csv_ios_path, 'w',encoding='utf-8') as new_file_ios:
    new_file_ios.write(new_csv_ios)


#FIM DA PRIMEIRA LIMPEZA




