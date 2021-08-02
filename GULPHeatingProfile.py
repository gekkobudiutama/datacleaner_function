# GULP Output Analyzer
# Find pattern from GULP MD Simulation Output
import pandas as pd
import matplotlib.pyplot as plt

mylines = []
with open('5_1260_TiO2_geoOpt.got', 'rt') as f:
    for myline in f:
        mylines.append(myline)
#print(mylines)

time = []
temperature = []
for a in mylines:
    if a[2:9] =='** Time':
        time.append(a[-14:-5])
    if a[7:28] == 'Temperature       (K)':
        temperature.append(a[31:-1])
        #print(temperature)
#print(len(time))
#print(temperature)

df = pd.DataFrame(temperature, time)
print(df)
df.to_csv('5_1260_TiO2_geoOpt.csv')
#print(time)