import urllib.request as ur
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# URL koji sadrži XML datoteku s mjerenjima:
url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=0&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017'

# Dohvaćanje i parsiranje XML podataka
airQualityHR = ur.urlopen(url).read()
root = ET.fromstring(airQualityHR)

# Inicijalizacija DataFrame-a
df = pd.DataFrame(columns=('mjerenje', 'vrijeme'))

# Punjenje DataFrame-a podacima iz XML-a
i = 0
while True:
    try:
        obj = root[i]
    except IndexError:
        break
    
    row = dict(zip(['mjerenje', 'vrijeme'], [obj[0].text, obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = df.append(row_s)
    df.at[i, 'mjerenje'] = float(df.at[i, 'mjerenje'])  # Ispravljanje načina dodavanja vrijednosti
    i += 1

# Konvertiranje vremena u datetime format
df['vrijeme'] = pd.to_datetime(df['vrijeme'], utc=True)

# Grupiranje po danu i računjanje dnevnog prosjeka koncentracije PM10
df_daily = df.resample('D', on='vrijeme').mean().dropna().reset_index()

# Iscrtavanje grafa
plt.figure(figsize=(10, 6))
plt.plot(df_daily['vrijeme'], df_daily['mjerenje'])
plt.xlabel('Datum')
plt.ylabel('PM10 koncentracija (µg/m³)')
plt.title('Dnevna koncentracija lebdećih čestica PM10 za 2017. godinu u Osijeku')
plt.show()

# Ispis tri datuma kada je koncentracija PM10 bila najveća
top_3_dates = df_daily.nlargest(3, 'mjerenje')
print("Tri datuma s najvećom koncentracijom PM10:")
print(top_3_dates[['vrijeme', 'mjerenje']])
