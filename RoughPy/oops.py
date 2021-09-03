
                                      #OOPs#
print("your first program (1) is here \n\n")
class rankcard:
    about="info"
    def __init__(self,name,mark,grade):
        self.mark=mark
        self.grade=grade
        self.name=name
    def character(self,c):
        return "the character of {} is {}".format(self.name,c)
r1=rankcard("arun",84,"a")
r2=rankcard("ram",95,"s")
print("this program is the {} of two persons".format(rankcard.about))
print("the mark and grade of {} is {} and {}".format(r1.name,r1.mark,r1.grade))
print("the mark and grade of {} is {} and {}".format(r2.name,r2.mark,r2.grade))
print(r1.character("soft"))
print(r2.character("rude"))



print("\n\n the next program (2) is here \n\n")
class example:
    def __init__(self):
        self.name="mahesh"
        self.age=19
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
e1=example()
e2=example()
e2.name="kavi"
#e2.age=20
print(e1.name,e1.age,"\n",e2.name,e2.age )
if e1.compare(e2):
    print("both ages are same")
else:
    print("both ages are different")




print("\n\n the next program (3) is here \n\n")
class student:
    school="cheran" #class/static variable
    def __init__(self,m1,m2,m3):
        self.m1=m1 #instance variable
        self.m2=m2
        self.m3=m3
    #instance method
    def avg(self,name):
        return ("the average of {} is {}".format(name,((self.m1+self.m2+self.m3)//3)))
    #class method
    @classmethod
    def school_name(cls):
        return cls.school
    #static method
    @staticmethod
    def info():
        print("blah blah blah")
s1=student(54,78,97)
s2=student(78,64,80)
print(s1.avg("mahesh"),"\n",s2.avg("kavi"),"\n",student.school_name())
student.info()
#print(student.school)  



print("\n\n the next program (4) is here \n\n")  
class example1:
    def __init__(self):
        self.name=input("Enter the datas required")
        self.age=int(input())
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
    def show(self):
        return self.name,self.age
        
e1=example1()
e2=example1()
print(e1.show(),"\n",e2.show())
if e1.compare(e2):
    print("both ages are same")
else:
    print("both ages are different")




print("\n\n the next program (5) is here \n\n")
class a:
    def f1(self):
        print("f1 is running")
    def f2(self):
        print("f2 is running")
class b:
    def f3(self):
        print("f3 is running")
    def f4(self):
        print("f4 is running")
class c(b,a):
    def f5(self):
        print("f5 is running")
    def f6(self):
        print("f6 is running")
aa=a()
bb=b()
cc=c()
aa.f1()
bb.f3()
cc.f1()




print("\n\n the next program (6) is here \n\n")
class a:
    def __init__(self):
        print("In init of class a")
class b(a):
    pass
a1=b()
##
class c:
    def __init__(self):
        print("In init of class c")
class d(c):
    def __init__(self):
        print("In init of class d")
a1=d()
##
class x:
    def __init__(self):
        print("In init of class x")
class e:
    def __init__(self):
        print("In init of class e")
class f(e,x):
    pass
a1=f()  
#If there are two sub classes , when we use super().__init__(), it will call the init of left sided sub class
#it excecutes from lef to right {METHOD RESOLUTION ORDER}




print("\n\n the next program (7) is here \n\n")
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
    def __mul__(self,other):
        m1=self.m1*other.m1
        m2=self.m2*other.m2
        s4=student(m1,m2)
        return s4
    def __gt__(self,other):
        s1=self.m1+self.m2
        s2=other.m1+other.m2
        if s1>s2:
            return "s1 is greater"
        else:
            return "s2 is greater"
    def __str__(self):
        return "{} {}".format(self.m1,self.m2)
s1=student(55,78)
s2=student(80,78)
s3=s1+s2
s4=s1*s2
print(s3.m1,s3.m2)
print(s4.m1,s4.m2)
print(s1>s2)
print(s3)






# =============================================================================
# duck typing
# method overriding=two methods with same name at different classes
# method overloading=two method with same name in one class, To achieve this use one method with none operators
# to pass different number of arguments
# =============================================================================



print("\n\n the next program (8) is here \n\n")
from threading import*
import time
class hello(Thread):
    def run(self):
        for i in range(20):
            print("hello")
            time.sleep(1)
class hi(Thread):
    def run(self):
        for i in range(20):
            print("hi")
            time.sleep(1)
obj1=hello()
obj2=hi()
obj1.start()
time.sleep(0.2)
obj2.start()
obj1.join()
obj2.join()
print("bye")
#here we want to call start , internally it will call run .... it as inbuilt run fun (only run)


print("\n\n the next program (9) is here \n\n")
class Person:
    def __init__(self,initialAge):
        if initialAge<0:
            print("Age is not valid, setting age to 0.")
            self.age=0
        else:
            self.age=initialAge

        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.age<13:
            print("You are young.")
        elif self.age in range (13,18):
            print("You are a teenager.")
        else:
            print("You are old.")

        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.age+=1
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

