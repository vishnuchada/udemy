#!/usr/bin/python
from __future__ import division 
class Line(object):
	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2	
	def distance(self):
		distance = (((self.coor2[0] - self.coor1[0])**2) + ((self.coor2[1] - self.coor1[1])**2))**0.5
		print distance
	def slope(self):
		slope = (self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0])
		print slope

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()
li.slope()

##########
class Cylinder():
	pi = 3.14
	def __init__(self,height=1,radius=1):
		self.height = height
		self.radius = radius
	def volume(self):
		volume = self.pi*(self.radius**2)*self.height
		print volume
	def surface_area(self):
		surface_area = 2*self.pi*((self.radius**2)+(self.radius*self.height)) 
		print surface_area

c = Cylinder(2,3)
c.volume()
c.surface_area()
