# Write a class representing two-dimensional vector (with x and y coordinates),
# which supports the following operations:
# 1. Addition of two vectors: v1 + v2
# 2. Subtraction of two vectors: v1 - v2
# 3. Dot product of two vectors:
#     a. Using operator v1 * v2
#     b. Using method v1.dot(v2)
#     c. Using class method Vector2d.dot(v1, v2)
# 4. Vector length property:
#     a. v.length
# 5. String representation: str(v)
import math


class Vector(object):
    """
    Vector class representing two-dimensional vector (with x and y coordinates)
    which supports the following operations:
     1. Addition of two vectors: v1 + v2
     2. Subtraction of two vectors: v1 - v2
     3. Dot product of two vectors:
         a. Using operator v1 * v2
         b. Using method v1.dot(v2)
         c. Using class method Vector2d.dot(v1, v2)
     4. Vector length property:
         a. v.length
     5. String representation: str(v)
     >>> vector2 = Vector(3, 4)
     >>> vector2.length
     5.0
     >>> vector1 = Vector(1, 3)
     >>> vector1
     <Vector:1.0,3.0>
     >>> print str(vector1)
     1.0,3.0
     >>> vector3 = vector1 + vector2
     >>> print vector3
     4.0,7.0
     >>> vector4 = vector1 - vector2
     >>> print vector4
     -2.0,-1.0
     >>> print vector1 * vector2
     15.0
     >>> print Vector.dot(vector1,vector2)
     15.0
     >>> print vector1.dot(vector2)
     15.0
    """

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.length = math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        if type(other) == type(self):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)

    def __sub__(self, other):
        if type(other) == type(self):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector(new_x, new_y)

    def __mul__(self, other):
        if type(other) == type(self):
            new_x = self.x * other.x
            new_y = self.y * other.y
            return new_x + new_y

    @classmethod
    def dot(cls, v1, v2):
        new_x = v1.x * v2.x
        new_y = v1.y * v2.y
        return new_x + new_y

    def dot(self, other):
        if type(other) == type(self):
            new_x = self.x * other.x
            new_y = self.y * other.y
            return new_x + new_y

    def __repr__(self):
        class_name = self.__class__.__name__
        return "<{}:{},{}>".format(class_name, self.x, self.y)

    def __str__(self):
        return "{},{}".format(self.x, self.y)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
