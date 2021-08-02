import pandas as pd

df = pd.read_csv('SiSiOx.csv')
print(df.shape)
a_list = []
f_list = []
for index, row in df.iterrows():
    if row['e'] < 0.380049:
            if row['a'] == 'Si1':
                a = 'Si2'
                f = 0
    else:
        a = row['a']
        f = row['f']
    a_list.append(a)
    f_list.append(f)

df['a'] = a_list
df['f'] = f_list
print(df)
df.to_csv("newSiSiOx-2.csv", sep='\t')

