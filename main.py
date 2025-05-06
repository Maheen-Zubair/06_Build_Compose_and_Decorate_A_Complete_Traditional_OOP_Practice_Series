#1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Object banake test karo
s1 = Student("Mahim", 95)
s1.display()

#------------------------------------------------------------------------------------------------

#2. Using cls
class Counter:
    object_count = 0

    def __init__(self):
        Counter.object_count += 1

    @classmethod
    def show_count(cls):
        print(f"Ab tak {cls.object_count} objects ban chuke hain.")
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.show_count()

#------------------------------------------------------------------------------------------------

#3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand 

    def start(self):       
        print(f"{self.brand} car has started!")

my_car = Car("Toyota")
print(my_car.brand)
my_car.start()

#------------------------------------------------------------------------------------------------

#4.  Class Variables and Class Methods
class Bank:
    bank_name = "HBL"  # Class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  

    def show(self):
        print(f"Bank ka naam: {self.bank_name}")

b1 = Bank()
b2 = Bank()

b1.show()        
Bank.change_bank_name("UBL")   
b2.show()       


#------------------------------------------------------------------------------------------------

#5. Static Variables and Static Methods
class Mathutils:
  @staticmethod
  def add(a,b):
    return a+b

print(Mathutils.add(2,4))


#------------------------------------------------------------------------------------------------

#6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger object created. (Constructor called)")

    def __del__(self):
        print("Logger object destroyed. (Destructor called)")

log = Logger()

del log


#------------------------------------------------------------------------------------------------

#7. Access Modifiers: Public, Private, and Protected
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public
        self._salary = salary       # Protected
        self.__ssn = ssn            # Private

emp = Employee("Ali", 50000, "123-45-6789")

print("Name (public):", emp.name)        
print("Salary (protected):", emp._salary) 
print("SSN (private):", emp.__ssn)        #error




#------------------------------------------------------------------------------------------------

#8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name  

    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name) 
        self.subject = subject  

    def teach(self):
        print(f"I teach {self.subject}")

teacher1 = Teacher("Ali", "Math")
teacher1.introduce()  
teacher1.teach()     



#------------------------------------------------------------------------------------------------

#9. Abstract Classes and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass 

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(4, 5)
print(f"Area of Rectangle: {rectangle.area()}")


#------------------------------------------------------------------------------------------------

#10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name  
        self.breed = breed  

    def bark(self):
        print(f"{self.name} says: Woof! I am a {self.breed}.")

my_dog = Dog("Buddy", "Golden Retriever")

my_dog.bark()  

#------------------------------------------------------------------------------------------------

#11. Class Methods
class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title  
        self.author = author  
        Book.increment_book_count()  

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1 

book1 = Book("Book One", "Author A")
book2 = Book("Book Two", "Author B")

print(f"Total books: {Book.total_books}")  


#------------------------------------------------------------------------------------------------

#12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(0))    
print(TemperatureConverter.celsius_to_fahrenheit(100)) 

#------------------------------------------------------------------------------------------------

#13. Composition
class Engine:
    def start(self):
        print("The engine has started!")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

my_engine = Engine()
my_car = Car(my_engine)
my_car.start_car()


#------------------------------------------------------------------------------------------------
#14. Aggregation
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self, employee):
        self.employee = employee  

    def show_department(self):
        print("Department mein jo employee hai:")
        self.employee.show()

emp1 = Employee("Mahim")
dept = Department(emp1)
dept.show_department()
emp1.show()


#------------------------------------------------------------------------------------------------

#15. Method Resolution Order (MRO) and Diamond Inheritance

class A:
    def show(self):
        print("Class A ka show method")

class B(A):
    def show(self):
        print("Class B ka show method")

class C(A):
    def show(self):
        print("Class C ka show method")

class D(B, C):
    pass 
obj = D()

# MRO checks,which method is called first
obj.show()  



#------------------------------------------------------------------------------------------------
#16. Function Decorators

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func() 
    return wrapper

@log_function_call
def say_hello():
    print("Hello, World!")

say_hello()

#------------------------------------------------------------------------------------------------

#17. Class Decorators

def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"  
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

p = Person("Mahim")

print(p.greet()) 

p.say_hello() 

#-------------------------------------------------------------------------------------------------

#18. Property Decorators: @property, @setter, and @deleter
class Product:
    def __init__(self, price):
        self._price = price 

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting price")
        del self._price

p = Product(100)

print(p.price)  
p.price = 200 
p.price = -50  
del p.price 

#--------------------------------------------------------------------------------------------------

#19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

m = Multiplier(5)
print(m(10))  
print(callable(m))


#--------------------------------------------------------------------------------------------------
#20. Creating a Custom Exception

class InvalidAgeError(Exception):  # Inherit from base Exception class
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")  # Raise custom exception if age is less than 18
    else:
        print("Access granted ✅")

try:
    check_age(16) 
except InvalidAgeError as e:
    print("Custom Exception:", e) 

#--------------------------------------------------------------------------------------------------

#21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.start = start 
    
    def __iter__(self):
        self.current = self.start  # Initialize current value to start
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop the iteration when 0 is reached
        else:
            self.current -= 1  # Decrease current value by 1
            return self.current 

count = Countdown(5)
for number in count:
    print(number) 




