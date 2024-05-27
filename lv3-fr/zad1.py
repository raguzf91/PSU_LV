import pandas as pd
import numpy as np

# Pretpostavljamo da imate mtcars.csv file, ako ne, možete ga preuzeti s interneta.
# Učitajmo mtcars dataset
df = pd.read_csv('mtcars.csv')

# Dodavanje naziva kolona ako nisu automatski prepoznati
df.columns = ['name', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

# 1. Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)
top_5_mpg = df.nlargest(5, 'mpg')
print("Top 5 automobila s najvećom potrošnjom:")
print(top_5_mpg[['name', 'mpg']])

# 2. Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
three_least_mpg_8cyl = df[df['cyl'] == 8].nsmallest(3, 'mpg')
print("Tri automobila s 8 cilindara s najmanjom potrošnjom:")
print(three_least_mpg_8cyl[['name', 'mpg']])

# 3. Kolika je srednja potrošnja automobila sa 6 cilindara?
mean_mpg_6cyl = df[df['cyl'] == 6]['mpg'].mean()
print("Srednja potrošnja automobila sa 6 cilindara:", mean_mpg_6cyl)

# 4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
mean_mpg_4cyl_2000_2200 = df[(df['cyl'] == 4) & (df['wt'] * 1000 >= 2000) & (df['wt'] * 1000 <= 2200)]['mpg'].mean()
print("Srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs:", mean_mpg_4cyl_2000_2200)

# 5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
num_manual = df[df['am'] == 1].shape[0]
num_automatic = df[df['am'] == 0].shape[0]
print("Broj automobila s ručnim mjenjačem:", num_manual)
print("Broj automobila s automatskim mjenjačem:", num_automatic)

# 6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
num_auto_hp_over_100 = df[(df['am'] == 0) & (df['hp'] > 100)].shape[0]
print("Broj automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga:", num_auto_hp_over_100)

# 7. Kolika je masa svakog automobila u kilogramima?
df['wt_kg'] = df['wt'] * 453.592  # 1 lb = 453.592 grams
print("Masa automobila u kilogramima:")
print(df[['name', 'wt_kg']])
