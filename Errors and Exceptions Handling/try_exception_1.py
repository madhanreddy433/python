print("First program on try block")

# try:
# 	pass
# except Exception as e:
# 	raise
# else:
# 	pass
# finally:
# 	pass				

while True:
	try:
		num1 = int(input("enter num1:"))
		num2 = int(input("enter num2:"))

		def add(num1, num2):
			return num1 + num2

	except:
		print("please enter integers only for addition")

	else:
		print("added successfully and sum is {}".format(add(num2,num1)))
		break

	finally:
		print("end of try/Exception/finally")

