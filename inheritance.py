# class A:
#     def greet(self):
#         print("Hello from A")

# class B(A):
#     def greet(self):
#         print("Hello from B")
#         super().greet()

# class C(A):
#     def greet(self):
#         print("Hello from C")
#         super().greet()

# class D(B, C):  # D inherits from B and C
#     def greet(self):
#         print("Hello from D")
#         super().greet()

# d = D()
# d.greet()

class Person:
    def __init__(self,name):
        self.name=name
        print(f"person initailized with name {name}")
    def position(self):
        print("person")

class Employee(Person):
    def __init__(self,name,employee_id):
        super(Employee,self).__init__(name)
        self.employee_id=employee_id
        print(f"person initailized with name {name} and id {employee_id}")
    def position(self):
        print("employee")    


class Teacher(Employee,Person):
    def __init__(self,name,employee_id,salary):
        self.salary=salary
        super(Teacher,self).__init__(name,employee_id)
        print(f"person initailized with name: {name} and id: {employee_id} and salary= {salary}")
       
teacher=Teacher("A","2d5",4500)
teacher.position()


print(Teacher.__mro__)

