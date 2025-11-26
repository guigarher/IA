import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv('masca.csv')
df.columns= ['Fecha', 'Origen', 'Visitantes']
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['mes'] = df['Fecha'].dt.month
df['dia_semana'] = df['Fecha'].dt.dayofweek


y = df['Visitantes']
X = df[['mes', 'dia_semana']]


test_size = 0.2

random_state = 42

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    


model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)



y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'MAE: {mae}')
print(f'R²: {r2}')


