import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


df = pd.read_csv('occupancy_processed.csv')
feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'

# Pretpostavljeni X i y
X = df[feature_names].values
y = df[target_name].values

# Podijeliti podatke na skup za učenje i skup za testiranje
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Skalirati ulazne veličine
# Izgraditi stablo odlučivanja
max_depth = 3  # dubina stabla
decision_tree = DecisionTreeClassifier(max_depth=max_depth)
decision_tree.fit(X_train, y_train)

# Evaluirati klasifikator na testnom skupu podataka
# Vizualizirajte dobiveno stablo odlučivanja
plt.figure(figsize=(10, 7))
plot_tree(decision_tree, feature_names=feature_names, class_names=['Slobodna', 'Zauzeta'], filled=True)
plt.show()

# Matrica zabune
y_pred = decision_tree.predict(X_test)
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matrica zabune:")
print(conf_matrix)

# Točnost klasifikacije
accuracy = accuracy_score(y_test, y_pred)
print("Točnost klasifikacije:", accuracy)

# Preciznost i odziv po klasama
precision_class_0 = precision_score(y_test, y_pred, pos_label=0)
precision_class_1 = precision_score(y_test, y_pred, pos_label=1)
recall_class_0 = recall_score(y_test, y_pred, pos_label=0)
recall_class_1 = recall_score(y_test, y_pred, pos_label=1)

print("Preciznost klase 'Slobodna':", precision_class_0)
print("Preciznost klase 'Zauzeta':", precision_class_1)
print("Odziv klase 'Slobodna':", recall_class_0)
print("Odziv klase 'Zauzeta':", recall_class_1)

#b
# Promjenom dubine stabla (max_depth) možemo kontrolirati složenost modela. 
# Povećanje dubine stabla može rezultirati složenijim modelom koji bolje 
# prilagođava podatke za učenje, ali može dovesti i do prenaučenosti. 
# Smanjenje dubine stabla može dovesti do jednostavnijeg modela s manje 
# sklonosti prenaučenosti, ali može rezultirati lošijim prilagođavanjem na podatke.

#c
# Za stablo odlučivanja, skaliranje ulaznih veličina nije potrebno jer stablo 
# odlučivanja ne ovisi o apsolutnim vrijednostima značajki, već o njihovim relativnim odnosima. 
# Stoga, rezultati ne bi trebali biti značajno različiti ako ne koristimo skaliranje ulaznih veličina.





