#2.Write a program that implements a Matrix class and performs addition, multiplication and transpose operations on 3x3 matrices.
class metrix:
    def __init__(self,arr=[]):
        self.arr=arr
    def prin(self):
        print(self.arr)
    def __add__(self,ob2):
        li=[]
        for i in range(3):
            l=[]
            for j in range(3):
                l.append(self.arr[i][j]+ob2.arr[i][j])
            li.append(l)
        return metrix(li)
    def __sub__(self,ob2):
        
        li=[]
        for i in range(3):
            l=[]
            for j in range(3):
                l.append(self.arr[i][j]-ob2.arr[i][j])
            li.append(l)
        return metrix(li)
    def trans(self):
        li=[]
        for i in range(3):
            l=[]
            for j in range(3):
                l.append(self.arr[j][i])
            li.append(l)
        return metrix(li)
    def multi(self,ob2):
        li=[]
        for k in range(3):
            l=[]
            for i in range(3):
                sum1=0
                for j in range(3):
                    sum1=sum1+(self.arr[k][j]*ob2.arr[j][k])
                l.append(sum1)   
            li.append(l)
        return metrix(li)
lis=[]
lis1=[]
print("enter first array")
for i in range(3):
    li=[]
    for j in range(3):
        a=int(input())
        li.append(a)
    lis.append(li)
print("enter unother array")
for i in range(3):
    li=[]
    for j in range(3):
        a=int(input())
        li.append(a)
    lis1.append(li)
ob1=metrix(lis)
ob2=metrix(lis1)
print(lis)
print(lis1)
ob3=ob1+ob2
print("matrix addition=",end="")
ob3.prin()
print("matrix substraction=",end="")
ob3=ob1-ob2
ob3.prin()
print("transpose of first matrix = ")
ob3= ob1.trans()
ob3.prin()
print("matrix multiplication=",end="")
ob3= ob1.multi(ob2)
ob3.prin()