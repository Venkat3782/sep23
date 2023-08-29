'''                 object oriented programming                        '''

# class(template)
'''
1.we will define class by using 'class' keyword
2.blue print to create a objects
3.collection of objects is called class
'''
#ex fruits
















# object
# physical entity(real)
'''
1.an instance of a class
2.memory is created when it declared
'''
#ex apple,orange,mango






# class Pramod():# class defination
#     # constructors
#     # functions
#     # variables


























# attribute (variable) data members
'''
age=20 
color='blue'
'''






















# method(behaviour) or functions , member functions
'''
eat() 
sleep()
'''
















# self keyword
'''
we can access the attributes and methods of the class(current class only)
'''

# class Sai(): # class defination
#     def class_fun(self):
#         print("this is class fun")
# # object name=Class name
# Obj=Sai()
# #obj.method
# Obj.class_fun()





















# class Karthik(): # class defination
#     def Output(self):
#         print("this is class")

# # object name = class name() object creation
# vivo=Karthik()
# vivo.Output() # methods access object name.method













# class Shiva():
#     a=10 
#     def show(self):
#         print("this is class")
# # obj name=class name()
# kiran=Shiva()
# print(kiran.a)
# kiran.show()





# class Srilekha(): # class defination
#     a=10
#     def ClassMethod(self):
#         print("this is class")
# # Obj name=Class name()
# kiranobj1=Srilekha()
# kiranobj=Srilekha() # object declaration
# kiranobj.ClassMethod()
# print(kiranobj.a)









# class James():
#     def display(self):
#         print('this is class')

# obj=James() # objectname=classname ()
# # objectname.method
# obj.display()









# class Kiran(): # class keyword class name
#     a=10 # data member
#     def Output(self): # method(self)
#         print(self.a)
# obj=Kiran()  # declaring of object 
# obj.Output() # using object we can call the methods  
















# class Naveen():
#     a=10 #attribute
#     def display(self):
#         print(self.a)
    
# ram=Naveen()  # object declaration
# # object name . method name ()
# syam=Naveen()
# ram.display()
# syam.display()

























# # # __init__

# # '''
# # Constructors are generally used for instantiating an object. 
# # The task of constructors is to initialize(assign values)
# # to the data members of the class when an object of the class 
# # is created.
# # In Python the __init__() method is called the constructor
# # and is always called when an object is created

# # does'nt support multiple constructor
# # '''




# a=100
# def fun1():
#     a=10
# fun1()
# def fun2():
#     d=a 
# fun2()




# class hemanth():
#     def __init__(self,a,b,c,d):
#         self.a=a 
#         self.b=b
#         self.c=c
#         self.d=d

#     def Test(self):
#         print(self.a,self.b,self.c,self.d)

# obj=hemanth(1,2,3,4)
# obj.Test()




# class Bike():
#     def __init__(self,Bike_Name,CC,Color,Price,Mileage):
#         self.b=Bike_Name
#         self.c=CC
#         self.d=Color
#         self.e=Price
#         self.f=Mileage
#     def Bike_Details(self):
#         print("Bike Name:",self.b)
#         print("Bike CC:",self.c)
#         print("Bike Color:",self.d)
#         print("Bike Price:",self.e)
#         print("Bike Mileage:",self.f)
# while True:
#     bn=input("Enter the Bike Name:")
#     bcc=input("Enter the Bike CC:")
#     bc=input("Enter the Bike Color:")
#     bp=input("Enter the Bike Price:")
#     bm=input("Enter the Bike Mileage:")
#     bikeobj=Bike(bn,bcc,bc,bp,bm)
#     bikeobj.Bike_Details()























# class Prakash():
#     def __init__(self,a,b,c):
#         self.ff=a
#         self.vv=b
#         self.dd=c
#         print(a)
#     def Output(self):
#         print(self.ff,self.vv,self.dd)
# p=Prakash(1,2,3)
# p.Output()


# class Mobiles():
#     def __init__(self,Mobile_name,Mobile_Ram,Mobile_battery,Mobile_Price):
#         self.a=Mobile_name
#         self.c=Mobile_Ram
#         self.d=Mobile_battery
#         self.e=Mobile_Price

#     def Mobile_Data(self):
#         print("Mobile Name:",self.a)
#         print("Mobile Ram:",self.c)
#         print("Mobile Battery:",self.d)
#         print("Mobile Price:",self.e)

# while True:
#     name=input("Enter the Mobile Name:")
#     ram=input("Enter the Mobile Ram:")
#     bat=input("Enter the Mobile Battery:")
#     Price=float(input("Enter the Mobile Price:"))

#     Mobile_obj=Mobiles(name,ram,bat,Price)
#     Mobile_obj.Mobile_Data()






































# class Lokesh():
#     def __init__(self,a,b,c):
#         self.kiran=a
#         self.f=b
#         self.v=c
#     def lakshmi(self):
#         print(self.kiran,self.f,self.v)

# lobj=Lokesh(1,2,3)
# lobj.lakshmi()


# class Laptop():
#     def __init__(self,Laptop_Model,Laptop_Company,Laptop_Price,Laptop_Ram,Laptop_Proccessor):
#         self.a=Laptop_Model
#         self.b=Laptop_Company
#         self.c=Laptop_Price
#         self.d=Laptop_Proccessor
#         self.e=Laptop_Ram
#     def laptop_details(self):
#         print("Laptop Model :",self.a)
#         print("Laptop Company :",self.b)
#         print("Laptop Price :",self.c)
#         print("Laptop Processor :",self.d)
#         print("Laptop Ram :",self.e)
# lm=input("Enter the Laptop Model: ")
# lc=input("Enter the Laptop Company: ")
# lp=input("Enter the Laptop Price: ")
# lpp=input("Enter the Laptop Processor: ")
# lr=input("Enter the Laptop Ram: ")
# obj=Laptop(lm,lc,lp,lpp,lr) 
# obj.laptop_details()     














# class Mobiles():
#     def __init__(self,Name,Price,Ram,Cam):
#         self.n=Name
#         self.c=Price
#         self.z=Ram
#         self.r=Cam
#     def Mobile_data(self):
#         print("Mobile Name:",self.n)
#         print("Mobile Price:",self.c)
#         print("Mobile Ram:",self.z)
#         print("Mobile Cam:",self.r)
# a=input("Enter the Mobile Name:")
# b=float(input("Enter the Mobile Price:"))
# c=input("Enter the Mobile Ram:")
# d=input("Enter the Mobile Cam:")
# mobile_obj=Mobiles(a,b,c,d)
# mobile_obj.Mobile_data()








# 











# class Laptop():
#     def __init__(self,Laptop_name,Model,Ram,Rom,Price):
#         self.a=Laptop_name
#         self.b=Model
#         self.c=Ram
#         self.d=Rom
#         self.e=Price
#     def Laptop_Info(self):
#         print("Name of the Laptop",self.a)
#         print("Model of the Laptop",self.b)
#         print("Ram of the Laptop",self.c)
#         print("Rom of the Laptop",self.d)
#         print("Price of the Laptop",self.e)
# name=input("Enter the laptop Name:")
# model=input("Enter the laptop Model:")
# ram=input("Enter the laptop Ram")
# rom=input("Enter the laptop Rom")
# price=float(input("Enter the laptop price:"))
# laptop_obj=Laptop(name,model,ram,rom,price)
# laptop_obj.Laptop_Info()














# class Sai:
#     def __init__(self,a,b,c):
#         # intialize
#         self.a=a
#         self.b=b
#         self.c=c
#     def kiran(self):
#         print(self.a,self.b,self.c)

# sb=Sai(2,3,4)
# sb.kiran()



# class Mobiles:
#     def __init__(self,Name,Ram,Rom,Cam,Battery,Price):
#         self.a=Name
#         self.b=Ram
#         self.c=Rom
#         self.d=Cam
#         self.e=Battery
#         self.f=Price
#     def Mobile_details(self):
#         print("Mobile Name",self.a)
#         print("Mobile Ram ",self.b)
#         print("Mobile Rom",self.c)
#         print("Mobile Cam",self.d)
#         print("Mobile Battery",self.e)
#         print("Mobile Price",self.f)
# mn=input("Enter the Mobile Name:")
# mr=int(input("Enter the Mobile Ram :"))
# mro=int(input("Enter the Mobile Rom:"))
# mc=input("Enter the Mobile Cam:")
# mb1=input("Enter the Mobile Battery:")
# mp=float(input("Enter the Mobile Price:"))
# mb=Mobiles(mn,mr,mro,mc,mb1,mp)

# mb.Mobile_details()














# class Naveen:
#     def __init__(self,a,b,c):
#         self.x=a #10
#         self.y=b # 1
#         self.f=c # 2
        
#     def display(self):
#         print(self.x)
#         print(self.f)
    
# ram=Naveen(10,1,2)  # object declaration
# # object name . method name ()
# ram.display()




# # class Mobiles:
# #     def __init__(self,Name,cam,Batt,Proces,price):
# #         self.c=Name
# #         self.x=cam
# #         self.b=Batt
# #         self.p=Proces
# #         self.a=price
# #     def output(self):
# #         print('Mobile Name:',self.c)
# #         print('Mobile Camera:',self.x)
# #         print('Mobile Battery:',self.b)
#         print('Mobile process:',self.p)
#         print('Mobile Price:',self.a)
# mn=input('Enter the Mobile Name:')
# mc=input('Enter the Mobile Camera:')
# mb=input('Enter the Mobile Battery:')
# mp=input('Enter the Mobile Process:')
# mpp=input('Enter the Mobile Price:')
# suresh=Mobiles(mn,mc,mb,mp,mpp)
# suresh.output()






# class Bikes: # class declaration or defination
#     def __init__(self,brand,mileage,cost,cc,color):
#         self.a=brand
#         self.x=mileage
#         self.z=cost
#         self.s=cc
#         self.j=color

#     def bike_details(self):
#         print('Bike Brand',self.a)
#         print('Bike Mileage',self.x)
#         print('Bike Cost',self.z)
#         print('Bike CC',self.s)
#         print('Bike Color',self.j)
    
# brands=input('Enter the Brand Name:')
# Mileages=input('Enter the Mileage:')
# Costs=float(input('Enter the Cost:'))
# ccs=input('Enter the CC:')
# colors=input('Enter the Colors:')
# Bike_obj=Bikes(brands,Mileages,Costs,ccs,colors)
# Bike_obj.bike_details()

        












# # inheritance
# # single (parent child)
# # multiple(two are more base classes)
# # # multilevel(tree)
# # # # hierarchical(one base with sibiling childs)










# class Parent:
#     def output(self):
#          print('this is parent class')     
# class Child(Parent):
#     def outputChild(self): # output
#         print('this is child class')
# i=Child()
# i.output()
# i.outputChild()






# class Father:
#     def output(self):
#         print('this is parent class')
# class Mother:
#     def outputM(self):
#         print('this is mother class')
# class Child(Father,Mother):
#     def outputChild(self):
#         print('this is child class')      
# ice=Child()
# ice.output()
# ice.outputM()
# ice.outputChild()



# class GrandFather:
#     def output(self):
#         print('this is gf class')
# class Father(GrandFather):
#     def outputf(self):
#         print('this is father class')
# class Child(Father):
#     def outputChild(self):
#         print('this is child class')      
# ice=Child()
# ice.output()
# ice.outputf()
# ice.outputChild()






# class Father:#100cr
#     def output(self):
#         print('this is father class')
# class Child1(Father):#50cr
#     def outputf(self):
#         print('this is child 1 class')
# class Child2(Father):#50cr
#     def outputChild(self):
#         print('this is child  2 class')      
# ice=Child1()
# cream=Child2()
# ice.output() #child 1 of parent
# ice.outputf()
# cream.output() # child 2 of parent
# cream.outputChild() # child 2




# class Father:#100cr
#     def output(self):
#         print('this is father class')
# class Child1(Father):#50cr
# #     def outputf(self):
# #         print('this is child 1 class')
# # obj=Father()
# # obj.outputf()



# class Father:
#     def funv(self):
#         print('this is father')

# class Mother:
#     def fun(self):
#         print('this is Mother')
# class Done:
#     def fun2(self):
#         print('this is class')









# class Child(Father,Mother,Done):
#     def func(self):
#         print('this is child')
# obj=Child()
# obj.funv()
# obj.fun()
# obj.func()
# obj.fun2()
































# Polymorphism
# poly-many
# morph = forms
# 1.method overloading 
# 2.method overridding

# def test(a,b):
#     print(a+b)

# test(1,1)
# test("k",'k')
# test([1,2],[3,4])











# class Methodoverlod:
#     def something(self,a=None,b=None,c=None):
#         print(a,b,c)
# obj=Methodoverlod()
# obj.something(1,2,3)
# obj.something(1,2)
# obj.something(1)
# obj.something()







# # research the different approuches to overcome the method overloading









# class Methodoverri:
#     def display(self):
#         print("this is parent class")

# class Child(Methodoverri):
#     def display(self):
#         print("this is child class")
#         super().display() 

# class Child2(Child):
#     def display(self):
#         print("this is child 2 class")
#         super().display() 
               
# obj=Child2()
# obj.display()
















#encapsulation

# binding of class (methods and variables(attributes))
# # public 
# # and 
# # private __
# # protected _
















# class GFather:
#     def __init__(self,a):
#         self._y=a
#         print(self._y)
# class Father(GFather):
#     def display1(self):
#         print(self._y)
# class Child2(Father):
#     def display2(self):
#         print("child2",self._y)
# obj=Child2(12)
# obj.display1()
# obj.display2()



# a=10
# def func():
#     b=20
#     print('this is fun',b,a)
# func()

# print(a)
















# #abstraction
#abstract method there is no body
#abstract base class can not  create object
#a class contain one or more abstract methods then it said to be a abc








# Python program demonstrate  
# abstract base class work  


# from abc import ABC, abstractmethod   
# class Car(ABC): 
#     @abstractmethod  
#     def mileage(self):   
#         pass  
# class Tesla(Car):   
#     def mileage(self):   
#         print("The mileage is 30kmph")   
# class Suzuki(Car):   
#     def mileage(self):   
#         print("The mileage is 25kmph ")   
# class Duster(Car):   
#      def mileage(self):   
#           print("The mileage is 24kmph ")   
# class Renault(Car):   
#     def mileage(self):   
#             print("The mileage is 27kmph ")           
# # # Driver code

# t= Tesla ()   
# t.mileage()   
# r = Renault()   
# r.mileage()    
# s = Suzuki()   
# s.mileage()   
# d = Duster()   
# d.mileage()  





