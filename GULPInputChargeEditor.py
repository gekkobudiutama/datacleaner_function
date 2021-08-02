import pandas as pd

df = pd.read_csv('csvfiles/k-3gin.csv', sep='\t', header=None)
print(df)
charge = []
for index, row in df.iterrows():
    if row[0] == "Si1":
        ch = 2.4
    if row[0] == "O1":
        ch = -1.2
    if row[0] == "Si2":
        ch = 2.4
    if row[0] == "O2":
        ch = -1.2
    if row[0] == "Ti1":
        ch = 2.4
    charge.append(ch)
print(charge)
df[5] = charge

print(df)
df.to_csv("csvfiles/k-3ginoutput.csv", sep='\t')