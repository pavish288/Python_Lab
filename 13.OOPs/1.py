#1.Write a program to create a class that represents Complex numbers containing real and imaginary parts and then use
#it to perform complex number addition, subtraction, multiplication and division.
class complx:
    def __init__(self,real=0,imag=0):
        self.real=real
        self.imag=imag
    def prin(self):
        print(f'{self.real} + {self.imag}i')
    def __add__(self,ob2):
        ob=complx()
        ob.real=self.real+ob2.real
        ob.imag=self.imag+ob2.imag
        return ob
    def __sub__(self,ob2):
        c=complx()
        c.real=self.real-ob2.real
        c.imag=self.imag-ob2.imag
        return c
    def __mul__(self,ob2):
        c=complx()
        c.real=(self.real * ob2.real)+ (self.imag*ob2.imag)
        c.imag=(self.imag * ob2.real)+ (self.real*ob2.imag)
        return c
    def __truediv__(self,ob2):
        c=complx()
        c.real=(self.real * ob2.real)+ (self.imag*ob2.imag)/((ob2.real)**2 + (ob2.imag)**2)
        c.imag=(self.imag * ob2.real)+ (self.real*ob2.imag)/((ob2.real)**2 + (ob2.imag)**2)
        return c
    
print("enter the complex no")
re=int(input("enter real part="))
imag=int(input("enter the image part="))
a=complx(re,imag)
a.prin()
o=complx(4,6)
ob3=a+o
print("addition=",end="")
ob3.prin()
ob4=a-o
print("subtraction=",end="")
ob4.prin()
ob4=a*o
print("multiplication=",end="")
ob4.prin()
ob4=a/o
print("division=",end="")
ob4.prin()