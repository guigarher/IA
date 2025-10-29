# Ficha rápida — Modelos de clasificación

| Modelo | Idea básica | Parámetro clave | Ventaja | Limitación |
|-------|-------------|-----------------|---------|------------|
| Naive Bayes | Aplica Bayes asumiendo independencia entre variables | Ninguno “crítico” (variante GaussianNB para continuas) | Muy rápido y robusto con pocos datos | Suposición de independencia rara vez se cumple |
| Árbol de Decisión | Divide el espacio con reglas “si-entonces” | `max_depth`, `min_samples_leaf` | Interpretables, manejan variables mixtas | Tienden a sobreajustar si no se podan |
| Bosque Aleatorio | Media muchos árboles aleatorios | `n_estimators`, `max_features` | Buen rendimiento general y robusto | Menos interpretable y más pesado que un árbol |
| KNN | Vota por los vecinos más cercanos | `n_neighbors (k)` | Simple y no entrena | Lento con muchos datos, sensible a escala |
| LDA | Proyección lineal que maximiza separación | — | Rápido y bien con clases gaussianas | Supone mismas covarianzas por clase |
| QDA | Como LDA pero con covarianzas distintas | — | Más flexible que LDA | Puede sobreajustar con pocos datos |
| SVM (linear) | Encuentra hiperplano con mayor margen | `C` | Muy fuerte en alta dimensión | Sensible a escala; lineal |
| SVM (rbf) | Mapea a espacio no lineal con kernel RBF | `C`, `gamma` | Capta fronteras complejas | Requiere ajustar hiperparámetros |
| MLP | Red neuronal feed-forward | `hidden_layer_sizes`, `alpha` | Modela no linealidades | Requiere más datos/tiempo y ajuste |

**Conclusiones de mi ejecución**
- Mejor modelo: *SVM (linear/rbf)* en Iris (diferencias pequeñas entre ambos).
- Peor modelo: *Árbol* sin ajustar hiperparámetros.
- Con Iris casi todos superan 0.93 de accuracy con test_size=0.5.
