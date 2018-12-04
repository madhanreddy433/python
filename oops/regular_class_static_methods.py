#regular methods: automatically takes instance as first argument (self)
#class methods: automatically takes class as first argument (cls)
#static methods: they don't pass anything(instance/class) automatically
					#they behave just like regular functions except we include them in class because they have some logical connection with class


class Employee:
	annual_raise = 1.04

	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.pay = pay

	def applay_raise(self):
		return self.pay * self.annual_raise

	@classmethod
	def change_raise_amount(cls, amount):
		cls.annual_raise = amount

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		else:
			return True

emp_1 = Employee('madhan', 'reddy', 40000)
emp_2 = Employee('suman', 'reddy', 50000)

print(Employee.annual_raise)
print(emp_1.annual_raise)
print(emp_1.annual_raise)

Employee.change_raise_amount(1.05)

print()

print(Employee.annual_raise)
print(emp_1.annual_raise)
print(emp_1.annual_raise)

Employee.annual_raise = 1.06

print()

print(Employee.annual_raise)
print(emp_1.annual_raise)
print(emp_1.annual_raise)

emp_1.change_raise_amount(1.07)		#running class methods on instances still changes all instance values
									#not recommended

print()

print(Employee.annual_raise)
print(emp_1.annual_raise)
print(emp_1.annual_raise)

import datetime
my_date = datetime.date(2018,12,3)

print()
print(Employee.is_workday(my_date))