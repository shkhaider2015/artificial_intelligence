class Employee:
   empCount = 0

   def __init__(self, name, salary, Age):
      self.name = name
      self.salary = salary
      self.Age = Age
      Employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)
   
   def displayEmployee(self):
      print("Name : "+ str(self.name)+  ", Salary: "+ str(self.salary)+ ", Age: "+ str(self.Age))
        
        
# This would create first object of Employee class
emp1 = Employee("Shakeel", 2000, 24)
# This would create second object of Employee class
emp2 = Employee("Salman", 5000, 27)

emp1.displayEmployee()
emp2.displayEmployee()