# -*- coding: utf-8 -*-

import math

class Polygon(object):

    def __str__(self):
        return "%s: %s" % (self.__shape_type, self.__shape)

    def __init__(self):
        self.__shape = {}
        self.__shape_type = 'polygon'

    def set_shape(self, poly):
        """Creates a polygon.

        Keyword arguments:
        poly -- should be tuple of tuples contaning vertex in (x, y) form.
            e.g. (  (0,0),
                    (0,1),
                    (1,1),
                    (1,0),
                )
        """
        assert type(()) == type(poly), "argument must be tuple of tuples."
        assert len(poly) > 1, "polygon must have more than one vertex."

        self.__shape['vertex_list'] = poly
        self.__shape['vertex_count'] = len(poly)


    def is_inside(self, point):
        """Returns True if the point lies inside the polygon, False otherwise.
        Works on Ray Casting Method (https://en.wikipedia.org/wiki/Point_in_polygon)

        Keyword arguments:
        point -- a tuple representing the coordinates of point to be tested in (x ,y) form.
        """
        poly = self.__shape['vertex_list']
        n = self.__shape['vertex_count']
        x, y = point
        inside = False

        p1x,p1y = poly[0]
        for i in range(n+1):
            p2x,p2y = poly[i % n]
            if y > min(p1y,p2y):
                if y <= max(p1y,p2y):
                    if x <= max(p1x,p2x):
                        if p1y != p2y:
                            xints = (y-p1y)*(p2x-p1x)/float(p2y-p1y)+p1x
                        if p1x == p2x or x <= xints:
                            inside = not inside
            p1x,p1y = p2x,p2y

        return inside



class Circle(object):

    def __str__(self):
        return "%s: %s" % (self.__shape_type, self.__shape)


    def __init__(self):
        self.__shape = {}
        self.__shape_type = 'circle'

    def set_shape(self, args):
        """Creates a circle.

        Keyword arguments:
        args -- will we a tuple of center and radius
            center should be tuple of coordinates in (x, y) form;
            radius should be scalar value represnting radius of the circle.
        """
        assert len(args) == 2, "there must be exactly two arguments."
        assert type(()) == type(args[0]), "first part of argument must be a tuple."
        assert args[1] > 0, "radius must be positive value."

        center = args[0]
        radius = args[1]
        self.__shape['center'] = center
        self.__shape['radius'] = radius


    def is_inside(self, point):
        """
            algo: we will calculate the distance of the point from the center of
            the circle and if it is <= radius we can say that point is inside the
            circle
        """
        x, y = point
        center_x, center_y = self.__shape['center']
        radius = self.__shape['radius']

        d = abs( math.sqrt( (center_x - x) ** 2 + (center_y + y) ** 2 ) )
        return d <= radius


class Geofence(object):

    def __str__(self):
        return str(self.__shape)

    def __init__(self, shape_type):
        shape_types = ['circle', 'polygon']
        assert shape_type in shape_types, "available geofence shapes are circle|polygon"
        if shape_type == 'circle':
            self.__shape  = Circle()
        elif shape_type == 'polygon':
            self.__shape = Polygon()

    def set_shape(self, *args):
        """Creates a Circle|Polygon depending on shape_type.

        Keyword arguments (in case of Circle):
        args -- will we a tuple of center and radius
            center should be tuple of coordinates in (x, y) form;
            radius should be scalar value represnting radius of the circle.

        Keyword arguments (in case of Polygon):
        poly -- should be tuple of tuples contaning vertex in (x, y) form.
            e.g. (  (0,0),
                    (0,1),
                    (1,1),
                    (1,0),
                )
        """
        self.__shape.set_shape(args)

    def get_shape(self):
        """Return the shape object Geofence(will be instance of Circle|Polygon)"""
        return self.__shape

    def get_shape_type(self):
        """Returns the shape_type of the geofence will be circle|polygon"""
        return self.__shape_type

    def is_inside(self, point):
        """Returns True if the point lies inside the geofence region.
        Keyword arguments:
        point - a tuple of coordinates in (x, y) form.
        """
        return self.__shape.is_inside(point)


if __name__ == "__main__":
    gfs = []

    g = Geofence('polygon')
    g.set_shape( ( 1, 1 ), ( 1, 2 ), ( 2, 2 ), ( 2, 1 ) )
    gfs.append(g)

    g = Geofence('circle')
    g.set_shape( ( 1 , 1 ), 3)
    gfs.append(g)

    for gf in gfs:
        print gf.get_shape()
        print gf.is_inside( ( 1.5, 1.5 ) )
        print gf.is_inside( ( 4.9, 1.2 ) )
        print gf.is_inside( ( 1.8, 1.1 ) )

