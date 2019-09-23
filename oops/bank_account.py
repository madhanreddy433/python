class Account:
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def deposit(self, amount):
		self.balance =  self.balance + amount
		print("{} is deposited and current balance is {}".format(amount, self.balance))

	def withdraw(self, amount):
		if amount > self.balance:
			print("insufficient amount \t available amount is {}".format(self.balance))

		else:
			self.balance = self.balance - amount
			print("{} is withdrawn and current balance is {}".format(amount, self.balance))

	def __str__(self):
		return "Account owner: {} \nAccount balanceis: {}".format(self.owner, self.balance)

accnt1 = Account('madhan', 1000)

print(accnt1)
print()
print(str(accnt1))
print()
print(accnt1.__str__())
print()

accnt1.withdraw(100)

accnt1.deposit(2000)

accnt1.withdraw(4000)




