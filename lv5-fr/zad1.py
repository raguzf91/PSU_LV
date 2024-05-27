import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Učitavanje podataka za učenje
df = pd.read_csv('occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

# Dijagram raspršenja
plt.figure()
for class_value in np.unique(y):
    mask = y == class_value
    plt.scatter(X[mask, 0], X[mask, 1], label=class_names[class_value])

plt.xlabel('S3_Temp')
plt.ylabel('S5_CO2')
plt.title('Zauzetost prostorije')
plt.legend()
plt.show()


#a
# Promatranjem dobivenog dijagrama raspršenja primjećujemo kako su podaci raspoređeni u odnosu na mjerenja 
# temperature i CO2 te kako su označeni prema zauzetosti prostorije. Izgleda da postoje dvije jasno odvojene 
# skupine podataka koje bi mogle odgovarati dvije klase - "Slobodna" i "Zauzeta" prostorija.

#b
num_examples = X.shape[0]
print("Broj podatkovnih primjera:", num_examples)

#c
num_class_0 = np.sum(y == 0)
num_class_1 = np.sum(y == 1)
print("Broj podatkovnih primjera u klasi 'Slobodna':", num_class_0)
print("Broj podatkovnih primjera u klasi 'Zauzeta':", num_class_1)
