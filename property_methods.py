class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary     #name and salary are only local inputs to methods which we pass out of the class 
                                #_name and _salary are the instance variables

    @property
    def salary_method(self):
        """Getter method for salary"""
        return self._salary

    @salary_method.setter
    def salary1(self, value):
        """Setter method for salary with validation"""
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

emp = Employee("Alice", 50000)
print(emp._salary)

emp.salary1 = 60000  # Update the salary using setter
print(emp._salary)