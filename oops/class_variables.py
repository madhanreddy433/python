class Employee:
	#class variables
	annual_raise = 1.04
	no_of_emp = 0

	def __init__(self, first_name, last_name, pay):
		Employee.no_of_emp += 1		#it will increment whenever we create an instance of this class
									#self.no_of_emp is different from Employee.no_of_emp

		self.first_name = first_name
		self.last_name = last_name
		self.pay = pay

	def ful_name(self):
		return "{} {}".format(self.first_name, self.last_name)

	def applay_raise(self):
		return self.pay * self.annual_raise

print("before creating instances no of employees are: {}".format(Employee.no_of_emp))

emp_1 = Employee('madhan', 'reddy', 50000)
emp_2 = Employee('suman' , 'reddy', 60000)

print(f"after creating instances no of employees are: {Employee.no_of_emp}")

print(emp_1.annual_raise)
print(emp_2.annual_raise)
print(Employee.applay_raise(emp_2))

emp_2.annual_raise = 1.05		#this change will apply only to instance emp_2 others remains same

print(emp_1.annual_raise)
print(emp_2.annual_raise)
print(Employee.applay_raise(emp_2))

Employee.annual_raise = 1.06	#this change will applys  to all the instances except emp_2 
								#because we changed the value of emp_2.annual_raise intentionally

print(emp_1.annual_raise)
print(emp_2.annual_raise)
print(Employee.applay_raise(emp_2))



	


