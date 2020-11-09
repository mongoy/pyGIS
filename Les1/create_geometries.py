from shapely.geometry import Point, LineString, Polygon
import random


# создадим точку
def CreatePointGeom(x_coord, y_coord):
    point = Point(x_coord, y_coord)
    print(type(point))
    return point


# создадим линию
def CreateLineGeom(points_count):
    # # генерация случайных пар координат точек
    # points = [(random.randrange(1, 10), random.randrange(1, 10)) for _ in range(points_count)]
    points = []
    for _ in range(points_count):
        coords_point = CreatePointGeom(random.randrange(1, 10), random.randrange(1, 10))
        if coords_point.geom_type == 'Point':  # проверка, это точка?
            points.append(coords_point)
    line = LineString(points)
    return line


def CreatePolyGeom():
    # генерация случайных пар координат точек
    points = [(random.randrange(1, 10), random.randrange(1, 10)) for _ in range(random.randrange(3, 10))]
    poly = Polygon(points)
    return poly


# print(CreatePointGeom(2, 3))
# print(CreateLineGeom(2))
# print(CreateLineGeom(3))
# print(CreateLineGeom(4))
print(CreatePolyGeom())
