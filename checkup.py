
# <-----no use ------->
import pandas
file = pandas.read_csv("database_total.csv",low_memory=False)
virus_md5 = file["md5"].tolist()
virus_name = file["name"]

# print(virus_name)
# print(virus_md5)
# print(type(virus_md5[4]))
# print(virus_name[10])
virus_signature = '01b656578e9f00f289d4c560fb8f2ff8'
if virus_signature in virus_md5:
    print("virus found")
    print(virus_md5.index(virus_signature))
    print(virus_name[int(virus_md5.index(virus_signature))])
else:
    print("not found")
