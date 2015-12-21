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
     >>> vector1 = Vector(0,0)
     >>> print vector1
     <Vector:0.0,0.0>
     >>> print str(vector1)
     <0.0,0.0>
    """

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        if type(other) == type(self):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)

    def __repr__(self):
        class_name = self.__class__.__name__
        return "<{}:{},{}>".format(class_name, self.x, self.y)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
