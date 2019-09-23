class Cylinder:
	pi = 3.14
	def __init__(self, height = 1, radius = 1):
		self.height = height
		self.radius = radius

	def volume(self):
		return self.pi * self.radius * self.radius * self.height	#pi*r*r

	def surface_area(self):
		return 2*self.pi*self.radius*(self.radius +	self.height)		#2*pi*r*(r+h)

cylinder1 = Cylinder(2,3)

print("cylinder1 area is {}".format(cylinder1.volume()))
print("cylinder1 surface area is {}".format(cylinder1.surface_area()))