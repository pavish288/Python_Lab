#3.Write a program to create a class that can calculate the surface area and volume of a solid.
#The class should also have a provision to accept the data relevant to the solid.
class solid:
    def __init__(self,l):
        self.len=l
    def volume(self):
        return (self.len)**3
    def area(self):
        return 6*(self.len)**2
l=int(input("enter the length of solid = "))
a=solid(l)
print("volume of solid = ",a.volume())
print("area of solid = ",a.area())