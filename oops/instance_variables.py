#python object oriented programming
class Employee:

	def __init__(self, first_name, last_name):
		self.first_name = first_name					#instance variables
		self.last_name = last_name
		self.email = first_name + '.' + last_name + '@company.com'

	def full_name(self):								#methods
		return "{} {}".format(self.first_name, self.last_name)

emp_1 = Employee('madhan', 'reddy')		#creating instance for Employee class
emp_2 = Employee(last_name = 'reddy', first_name = 'suman')

print(type(emp_1))

print(emp_1.full_name())		#calling instance methods
print(emp_1.email)				#calling instance variables

print(Employee.full_name(emp_2))	#another way of calling methods using class name, we should pass instance as attribute because all the methods
									#will accept instance as its first argument

