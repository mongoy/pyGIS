import os
import pandas as pd
from shapely.geometry import Point, LineString, Polygon

ROOT_PATH = os.path.abspath(os.curdir)  # текущая директорю, где запущен скрипт
file_path = os.path.join(ROOT_PATH, "InputData\\travelTimes_2015_Helsinki.txt")
# полный датафрейм
df = pd.read_csv(file_path, encoding="cp1251", sep=";")


def TravelLineString(data_frame):
    # датафрейм с координатами начала пути
    df_orig = df[["from_x", "from_y"]]
    # датафрейм с координатами окончания пути
    df_dest = df[["to_x", "to_y"]]
    # датафреймы в списки последовательностй, кортежи координат точек
    orig_points = list(zip(*map(df_orig.get, df_orig)))
    dest_points = list(zip(*map(df_dest.get, df_dest)))
    # список с координатами линий
    lines = []
    line = tuple()
    #
    for i in range(len(orig_points)):
        line = (orig_points[i], dest_points[i])
        lines += line
    line_string = LineString(lines)
    return line_string


def CalcAverageDist():
    """
        :return: Среднее (Евклидово) расстояние, для всех линий
    """
    print(TravelLineString(df))
    print(len(TravelLineString(df)))
    print(len(TravelLineString(df)) / 2)

    # for i in range(len(TravelLineString(df)) / 2):


CalcAverageDist()

