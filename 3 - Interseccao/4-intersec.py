from csv_diff import load_csv, compare
from pprint import pprint
import pandas as pd


diff = compare(
    load_csv(open("android_titles_limpo.csv",encoding="utf-8"), key="title"),
    load_csv(open("ios_titles_limpo.csv",encoding="utf-8"), key="title"),show_unchanged=True
)



with open("result_titles.json","w",encoding="utf-8",) as arq_result:
    pprint(diff,arq_result)







#pprint(df.head())







