# 7kyu - Building Spheres

""" Now that we have a Block let's move on to something slightly more complex a Sphere.

#Arguments for the constructor

radius -> integer or float (do not round it)
mass -> integer or float (do not round it)

#Methods to be defined

get_radius()       =>  radius of the Sphere (do not round it)
get_mass()         =>  mass of the Sphere (do not round it)
get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)

##Example

ball = Sphere(2,50)
ball.get_radius() ->       2
ball.get_mass() ->         50
ball.get_volume() ->       33.51032
ball.get_surface_area() -> 50.26548
ball.get_density() ->      1.49208 """

# from math import pi

# class Sphere:
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass

#     def get_radius(self):
#         return self.radius

#     def get_mass(self):
#         return self.mass

#     def get_volume(self):
#         self.volume = (4 / 3) * pi * self.radius ** 3
#         return float('{0:.5f}'.format(self.volume))

#     def get_surface_area(self):
#         self.surface_area = 4 * pi * self.radius ** 2
#         return float('{0:.5f}'.format(self.surface_area))

#     def get_density(self):
#         self.density = self.mass / self.volume
#         return float('{0:.5f}'.format(self.density))

from math import pi

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        self.volume = (4 / 3) * pi * self.radius ** 3
        return round(self.volume, 5)

    def get_surface_area(self):
        self.surface_area = 4 * pi * self.radius ** 2
        return round(self.surface_area, 5)

    def get_density(self):
        self.density = self.mass / self.volume
        return round(self.density, 5)


ball = Sphere(2, 50)

q = ball.get_radius()  # 2, "Check radius"
q
q = ball.get_mass()  # 50, "Check mass"
q
q = ball.get_volume()  # 33.51032, "Check volume"
q
q = ball.get_surface_area()  # 50.26548, "Check area"
q
q = ball.get_density()  # 1.49208, "Check density"
q
