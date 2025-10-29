# comparacion_modelos.py
# -------------------------------------------------------------
# Clasificación supervisada — Comparación de modelos (Iris)
# Guillermo García Hernández - 2º DAW
# Ejecuta: python comparacion_modelos.py
# -------------------------------------------------------------
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA, QuadraticDiscriminantAnalysis as QDA
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# 1) Datos
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0, stratify=y)

# 2) Modelos a comparar (nombre, instancia)
modelos = [
    ("Naive Bayes", GaussianNB()),
    ("LDA", LDA()),
    ("QDA", QDA()),
    ("Árbol", DecisionTreeClassifier(random_state=0)),
    ("Bosque", RandomForestClassifier(n_estimators=200, random_state=0)),
    ("KNN (k=5)", KNeighborsClassifier(n_neighbors=5)),
    ("SVM linear", SVC(kernel="linear", gamma="scale", C=1)),
    ("SVM rbf", SVC(kernel="rbf", gamma="scale", C=1)),
    ("MLP", MLPClassifier(hidden_layer_sizes=(50,), max_iter=1000, random_state=0)),
]

scores = {}
for name, clf in modelos:
    clf.fit(X_train, y_train)
    acc = accuracy_score(y_test, clf.predict(X_test))
    scores[name] = acc
    print(f"{name:12s}: {acc:.4f}")

# 3) Gráfico (guardado en PNG)
plt.figure(figsize=(9,5))
plt.barh(list(scores.keys()), list(scores.values()))
plt.xlabel("Precisión (accuracy)")
plt.title("Comparación de clasificadores — Iris (test_size=0.5)")
plt.xlim(0.8, 1.0)
plt.grid(axis='x', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("comparacion_iris.png", dpi=150)
print("→ Figura guardada: comparacion_iris.png")

# 4) Conclusión breve impresa
mejor = max(scores, key=scores.get)
peor = min(scores, key=scores.get)
print(f"Mejor modelo en mi ejecución: {mejor} (accuracy={scores[mejor]:.3f})")
print(f"Más flojo en mi ejecución:   {peor} (accuracy={scores[peor]:.3f})")
print("\\nNota: con Iris casi todos van muy bien; diferencias pequeñas pueden deberse a la partición de train/test.")
