import math as mh


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = self.__initialize_sides(sides)
        self.filled = False

    def __initialize_sides(self, sides):
        if len(sides) != self.sides_count:
            return [1] * self.sides_count
        return list(sides)

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False

    def __is_valid_sides(self, *new_sides):
        if self.sides_count != len(new_sides):
            return False
        for i in new_sides:
            if not isinstance(i, int) or i <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        circumference = self.get_sides()[0]
        return circumference / (2 * mh.pi)

    def get_square(self):
        return mh.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return mh.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * 12
        super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
#
# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
