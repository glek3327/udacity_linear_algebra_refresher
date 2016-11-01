
from math import sqrt, acos, pi, degrees
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG ='Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        # new_coordinates = []
        # n = len(self.coordinates)
        # for i in range(n)
        #     new_coordinates.append(self.coordinates[i], v.coordinates[i])
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        # sum = 0
        # for i in range(self.dimension):
        #     sum += pow(self.coordinates[i], 2)
        # return math.sqrt(sum)
        coordinates_squared = [x**2 for x in self.coordinates]
        return Decimal(sqrt(sum(coordinates_squared)))

    def nomalized(self):
        # return self.times_scalar(1 / self.magnitude())
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal(1.0)/magnitude)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot(self, v):
        return sum([x*y for x , y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        # normalized = self.nomalized()
        # return acos(normalized.dot(v.nomalized()))
        try:
            u1 = self.nomalized()
            u2 = v.nomalized()
            angle_in_radians = acos(u1.dot(u2))

            if in_degrees:
                degrees_per_radian = 180./ pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e

    def isParallel(self, v):
        # try:
            return self.angle_with(v) == 0
        # except Exception as e:
        #     print("error")
        #     return False

    def isOrthogonal(self, v):
        return self.dot(v) == 0


##vector module
# my_vector = Vector([1, 2, 3])
# print(my_vector)
# my_vector2 = Vector([1, 2, 3])
# my_vector3 = Vector([-1, 2, 3])
# print(my_vector == my_vector2)
# print(my_vector == my_vector3)

##quiz2
# vector1 = Vector([8.218, -9.341])
# vector2 = Vector([-1.129, 2.111])
# print(vector1.plus(vector2))
#
# vector1 = Vector([7.119, 8.215])
# vector2 = Vector([-8.223, 0.878])
# print(vector1.minus(vector2))
#
# vector1 = Vector([1.671, -1.012, -0.318])
# print(vector1.times_scalar(7.41))

##quiz 3
# vector1 = Vector([-0.221, 7.437])
# print(vector1.magnitude())
#
# vector1 = Vector([8.813, -1.331, -6.247])
# print(vector1.magnitude())
#
# vector1 = Vector([5.581, -2.136])
# print(vector1.nomalize())
#
# vector1 = Vector([1.996, 3.108, -4.554])
# print(vector1.nomalize())

##quiz4
# v = Vector([7.887, 4.138])
# w = Vector([-8.802, 6.776])
# print(v.dot(w))
#
# v = Vector([-5.955, -4.904, -1.874])
# w = Vector([-4.496, -8.755, 7.103])
# print(v.dot(w))
#
# v = Vector([3.183, -7.627])
# w = Vector([-2.668, 5.319])
# print(v.angle_with(w))
#
# v = Vector([7.35, 0.221, 5.188])
# w = Vector([2.751, 8.259, 3.985])
# print(degrees(v.angle_with(w)))

## quiz 5 : Checking for Parallelism & Orthogonality
v = Vector([-7.579, -7.88])
w = Vector([22.737, 23.64])
print(v.isParallel(w), v.isOrthogonal(w))

v = Vector([-2.029, 9.97, 4.172])
w = Vector([-9.231, -6.639, -7.245])
print(v.isParallel(w), v.isOrthogonal(w))

v = Vector([-2.328, -7.284, -1.214])
w = Vector([-1.821, 1.072, -2.94])
print(v.isParallel(w), v.isOrthogonal(w))

v = Vector([2.118, 4.827])
w = Vector([0, 0])
print(v.isParallel(w), v.isOrthogonal(w))