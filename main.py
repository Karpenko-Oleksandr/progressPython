class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Coords can be number type")

    def get_coord(self):
        return self.__x, self.__y

test_point = Point(1, 2)
test_point.set_coord(10, 20)
print(test_point.get_coord())