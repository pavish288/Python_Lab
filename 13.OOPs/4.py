class shap:
    def __init__(self,shap):
        self.shap=shap
        
    def area(self):
        if(self.shap=="circle"):
            a=int(input("enter the radius="))
            print("the peramiter is=",2*3.14*a,"\n the area is=",3.14*(a**2))
        if(self.shap=="squar"):
            a=int(input("enter the side length="))
            print("the peramiter is=",a*4,"\n the area is=",(a**2))
        if(self.shap=="rectangle"):
            a=int(input("enter the side length="))
            b=int(input("enter the side weidht="))
            print("the peramiter is=",2(a+b),"\n the area is=",(a*b))
        
a=input("enter the shap=")
s=shap(a)
s.area()