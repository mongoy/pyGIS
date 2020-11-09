import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
from fiona.crs import from_epsg


ROOT_PATH = os.path.abspath(os.curdir)
# Создадим пустой геодатафраме
new_data = gpd.GeoDataFrame()
# добавим колонку 'geometry'
new_data['geometry'] = None
# координаты в десятичных градусах
coordinates = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
# Создадим полигон
poly = Polygon(coordinates)
# добавим полигон в датафрэйм значение в строку 0
new_data.loc[0, 'geometry'] = poly
# добавим колонку 'location' + значение в строку 0
new_data.loc[0, 'location'] = 'Senaatintori'
# Определяем систему координат
print(new_data.crs)  # ПУСТО
# Установите систему координат GeoDataFrame в WGS84
new_data.crs = from_epsg(4326)

# Новый SHP-файл из датафрэйма
file_new = os.path.join(ROOT_PATH, "Output\\Data\\Senaatintori.shp")
new_data.to_file(file_new)

