# operator overloading

class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        return self.salary * other.days

class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days

e1 = Employee("bharathi", 1000)
ts = TimeSheet("bharathi", 28)     

print(e1 * ts)