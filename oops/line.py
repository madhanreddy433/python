class Line:
	def __init__(self, coordinate1, coordinate2):	#cordinates are tuples ex:(2,3)
		self.coordinate1 = coordinate1
		self.coordinate2 = coordinate2

	def distance(self):
		import math
		return math.sqrt(((coordinate2[1] - coordinate1[1])**2) + ((coordinate2[0] - coordinate1[0])**2))

	def slope(self):
		return ((coordinate2[1] - coordinate1[1])/(coordinate2[0] - coordinate1[0]))

coordinate1 = (3,2)
coordinate2 = (8,10)

line1 = Line(coordinate1, coordinate2)

print("distance between coordinate1 and coordinate2 is {}".format(line1.distance()))
print("slope between coordinate1 and coordinate2 is {}".format(line1.slope()))
