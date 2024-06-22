import pandas as pd

df = pd.read_csv('dz.csv')

# Группировка данных по городу и вычисление средней зарплаты
average_salary_by_city = df.groupby('City')['Salary'].mean()

# Вывод результата
print(average_salary_by_city)