class Employee:
	
	annual_raise = 1.04

	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.pay = pay

	def ful_name(self):
		return "{} {}".format(self.first_name, self.last_name)

	def emp_email(self):
		return "{}{}@company.com".format(self.first_name, self.last_name)

	def applay_raise(self):
		return self.pay * self.annual_raise

class Developer(Employee):				#Developer class inherited from Employee class
	
	annual_raise = 1.10

	def __init__(self, first_name, last_name, pay, prog_lang):
		super().__init__(first_name, last_name, pay)
		self.prog_lang = prog_lang

	def emp_email(self):				#we can able to over write the parent class methods
		return "{}{}.dev@company.com".format(self.first_name, self.last_name)



emp_1 = Employee('madhan', 'reddy', 30000)
dev_1 = Developer('suman', 'reddy', 40000, 'python')

print(Employee.annual_raise)
print(emp_1.applay_raise())

print()
print(Developer.annual_raise)
print(dev_1.applay_raise())		#developer class has its own annual_raise 
								#it over write the annual_rase of Employee class

print(dev_1.prog_lang)

print(emp_1.emp_email())
print(dev_1.emp_email())


