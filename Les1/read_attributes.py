from shapely.geometry import Point, LineString, Polygon
from Les1.create_geometries import CreatePolyGeom, CreateLineGeom, CreatePointGeom


def getCentroid():
    """
       :return: координаты центроида
    """
    poly = CreatePolyGeom()
    poly_centroid = poly.centroid
    return poly_centroid


def getArea():
    """
       :return: пощадь
    """
    poly = CreatePolyGeom()
    poly_area = poly.area
    return poly_area


def getLength(geom_obj):
    """
       :return: длина линии или внешнего контура
    """
    if geom_obj.geom_type == 'LineString':  # проверка, это линия?
        print(geom_obj)
        length_obj = geom_obj.length
        rezult = 'Длина линии - {0:.2f}'.format(length_obj)
    elif geom_obj.geom_type == 'Polygon':  # проверка, это полигон?
        print(geom_obj)
        length_obj = geom_obj.length
        rezult = 'Длина внешнего контура полигона - {0:.2f}'.format(length_obj)
    else:
        rezult = 'Error: LineString or Polygon geometries required!'

    return rezult


# print('Центроид полигона: ', getCentroid())
# print('Площадь полигона: ', getArea())

print(getLength(CreateLineGeom(2)))
print(getLength(CreatePolyGeom()))
print(getLength(CreatePointGeom(2, 3)))
