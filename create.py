import os
import pandas
import md5_generate

file = pandas.read_csv("out.csv",low_memory=False)
virus_md5=[]
for i in file["name"]:
    virus_md5.append(i[2:-1])

file["namenew"]=virus_md5
file.to_csv("out.csv")
