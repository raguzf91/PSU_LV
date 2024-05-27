import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Učitavanje mtcars dataset-a
df = pd.read_csv('mtcars.csv')

# Dodavanje naziva kolona ako nisu automatski prepoznati
df.columns = ['name', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

# Postavljanje stilova za grafove
sns.set(style="whitegrid")

# 1. Barplot - potrošnja automobila s 4, 6 i 8 cilindara
plt.figure(figsize=(10, 6))
sns.barplot(x='cyl', y='mpg', data=df, ci=None)
plt.title('Potrošnja automobila prema broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Potrošnja (mpg)')
plt.show()

# 2. Boxplot - distribucija težine automobila s 4, 6 i 8 cilindara
plt.figure(figsize=(10, 6))
sns.boxplot(x='cyl', y='wt', data=df)
plt.title('Distribucija težine automobila prema broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Težina (1000 lbs)')
plt.show()

# 3. Scatterplot - potrošnja automobila s ručnim i automatskim mjenjačem
plt.figure(figsize=(10, 6))
sns.boxplot(x='am', y='mpg', data=df)
plt.title('Potrošnja automobila prema tipu mjenjača')
plt.xlabel('Tip mjenjača (0 = automatski, 1 = ručni)')
plt.ylabel('Potrošnja (mpg)')
plt.xticks([0, 1], ['Automatski', 'Ručni'])
plt.show()

# 4. Scatterplot - odnos ubrzanja i snage automobila za različite tipove mjenjača
plt.figure(figsize=(10, 6))
sns.scatterplot(x='hp', y='qsec', hue='am', style='am', data=df, palette=['red', 'blue'])
plt.title('Odnos ubrzanja i snage automobila prema tipu mjenjača')
plt.xlabel('Snaga (konjskih snaga)')
plt.ylabel('Ubrzanje (kvartalna sekunda)')
plt.legend(title='Tip mjenjača', labels=['Automatski', 'Ručni'])
plt.show()
