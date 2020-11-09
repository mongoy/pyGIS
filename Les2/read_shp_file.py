import os
import numpy as np
import geopandas as gpd


# print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
# print("PATH:", os.environ.get('PATH'))

ROOT_PATH = os.path.abspath(os.curdir)
# file_path = os.path.join(ROOT_PATH, "Input\\Data\\DAMSELFISH_distributions.shp")

# Чтение SHP-файла
file_path = os.path.join(ROOT_PATH, "Input\\Data\\gran_admin.shp")
data = gpd.read_file(file_path)
# Сведения о датафрейме
print(data.info)
# Подсчёт количества элементов
print(data.type.value_counts())
# 5 первых
print(data['geometry'].head(5))
# 5 последних
print(data['geometry'].tail(5))
# число строк
print(len(data))

# Новый SHP-файл
# file_new = os.path.join(ROOT_PATH, "Output\\Data\\gran_admin_new.shp")
# selection = data[:50]
# selection.to_file(file_new)


# Площадь 5и первых объектов
selection = data[:5]
for index, row in selection.iterrows():
    poly_area = row['geometry'].area
    print("Площадь полигона {0} : {1:.3f}".format(index, poly_area))

# Добавим столбец для площади полигона
data['area'] = data.area
max_area = data['area'].max()
min_area = data['area'].min()
mean_area = data['area'].mean()
print('Квадратные десятичные градусы')
print("Максимальная площадь: %s\nМинимальная площадь: %s\nСредняя площадь: %s" % (round(max_area, 2), round(min_area, 2), round(mean_area, 2)))


