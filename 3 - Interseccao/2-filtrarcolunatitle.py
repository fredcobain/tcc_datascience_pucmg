#Esse código pega os arquivos CSV e extrai somente a coluna title para futura comparação

from csv_diff import compare
from pprint import pprint
import pandas as pd


df_ios = pd.read_csv("ios_apps_br_limpo.csv",encoding="utf-8")
df_android = pd.read_csv("android_apps_br_limpo.csv",encoding="utf-8")

header = ["title"]

df_ios.to_csv("ios_titles_2.csv",columns=header)
df_android.to_csv("android_titles_2.csv",columns=header)



#df_titles = pd.read_json("titles_result.json",encoding="utf-8")
#pprint(df.head())
#diff = compare(,"",show_unchanged=True)
