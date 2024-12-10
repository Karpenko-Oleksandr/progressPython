class Circle:
    def __init__(self, radius):
        if not self.is_valid_radius(radius):
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

    @classmethod
    def from_diameter(cls, diameter):
        if not cls.is_valid_radius(diameter / 2):
            raise ValueError("Radius derived from diameter must be positive.")
        return cls(diameter / 2)

    @staticmethod
    def is_valid_radius(value):
        return isinstance(value, (int, float)) and value > 0


try:
    circle = Circle.from_diameter(10)
    print(f"Radius: {circle.radius}")
    print(f"Area: {circle.area()}")
    print(f"Circumference: {circle.circumference()}")

    print(Circle.is_valid_radius(-5))
except ValueError as e:
    print(e)
