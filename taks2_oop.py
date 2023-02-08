class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * self.length + 2 * self.width

    def area(self):
        return self.length * self.width

    def display(self):
        print(f"length is {self.length} and width is {self.width}")
        print(f"perimeter is {self.get_perimeter()} and the area is {self.area()}  ")


class Parallelepipede(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        print("volume of the parallepipede is " + self.length * self.width * self.height)


a = Rectangle(5, 6)
a.display()
p = Parallelepipede(5, 6, 8)
p.volume()
