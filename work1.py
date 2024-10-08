import pandas as pd

# Создание DataFrame с оценками 10 учеников по 5 предметам
data = {
    'Имя': ['Ученик1', 'Ученик2', 'Ученик3', 'Ученик4', 'Ученик5', 'Ученик6', 'Ученик7', 'Ученик8', 'Ученик9', 'Ученик10'],
    'Математика': [85, 78, 92, 88, 76, 95, 89, 84, 91, 87],
    'Физика': [78, 74, 82, 88, 73, 85, 80, 77, 90, 84],
    'Химия': [90, 80, 88, 85, 70, 91, 87, 83, 78, 89],
    'Литература': [95, 89, 92, 91, 88, 90, 86, 85, 87, 93],
    'История': [78, 84, 85, 90, 79, 82, 88, 91, 87, 83]
}
df = pd.DataFrame(data)

# Переформатируем данные так, чтобы предметы стали одной колонкой
df_long = pd.melt(df, id_vars=['Имя'], var_name='Предмет', value_name='Оценка')

# Средняя оценка по каждому предмету
mean_scores = df_long.groupby('Предмет')['Оценка'].mean()
print("Средняя оценка по каждому предмету:")
print(mean_scores)

# Медианная оценка по каждому предмету
median_scores = df_long.groupby('Предмет')['Оценка'].median()
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Q1 и Q3 для оценок по математике
Q1_math = df_long[df_long['Предмет'] == 'Математика']['Оценка'].quantile(0.25)
Q3_math = df_long[df_long['Предмет'] == 'Математика']['Оценка'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print("\nПервый квартиль (Q1) для оценок по математике:", Q1_math)
print("Третий квартиль (Q3) для оценок по математике:", Q3_math)
print("Межквартильный размах (IQR) для оценок по математике:", IQR_math)

# Стандартное отклонение по каждому предмету
std_dev_scores = df_long.groupby('Предмет')['Оценка'].std()
print("\nСтандартное отклонение по каждому предмету:")
print(std_dev_scores)
