#!/usr/bin/python
# filename: simulation.py
# author: Latrokles -- latrokles@gmail.com
# description: Simple particle physics simulation

from pyglet.gl import *
from pyglet import window

class Vector:
	"""Simple Vector Class"""
	def __init__(self, data):
		self.data = data

	def __repr__(self):
		return repr(self.data)

	def __add__(self, other):
		data =[]
		for index in range(len(self.data)):
			data.append(self.data[index] + other.data[index])
		
		return Vector(data)



class Simulation:
	"""Main Particle Simulation System"""
	def __init__(self, gravity, drag):
		self.window = window.Window(caption='Simulation')
		self.gravity = gravity
		self.drag    = drag
		self.particles  = []
		self.window.on_mouse_press = self.on_mouse_press

	def __repr__(self):
		return 'Simulation parameters:\nGravity:\t%d\nDrag:\t%d' % (self.gravity, self.drag)

	def on_mouse_press(self, x, y, button, modifiers):
		self.particles.append(Rectangle(x, y, 0, Vector([0,0,0]), 10, 10))
	
	def on_mouse_motion(self, x, y, dx, dy):
		raise NotImplementedError

	def draw_particles(self):
		for particle in self.particles:
			particle.draw()

	def run(self):
		while not self.window.has_exit:
			self.window.dispatch_events()
			glClear(GL_COLOR_BUFFER_BIT)
			glLoadIdentity()

			self.draw_particles()

			self.window.flip()

class Particle:
	"""Defines a single particle, either 2D or 3D"""
	def __init__(self, x=0, y=0, z=0, direction=Vector([0,0,0])):
		self.x = x
		self.y = y
		self.z = z
		self.direction = direction

	def get_coordinates(self):
		return (self.x, self.y, self.z)

	def update_coordinates(self, dx=0, dy=0, dz=0):
		self.x += dx
		self.y += dy
		self.z += dy

	def draw(self):
		raise NotImplementedError

class Rectangle(Particle):
	def __init__(self, x=0, y=0, z=0, direction=Vector([0,0,0]), w=0, h=0):
		Particle.__init__(self, x, y, z, direction)
		self.width  = w
		self.height = h
	
	def draw(self):
		glBegin(GL_QUADS)
		glVertex2f(self.x - (self.width/2.0), self.y - (self.height/2.0))
		glVertex2f(self.x - (self.width/2.0), self.y + (self.height/2.0))
		glVertex2f(self.x + (self.width/2.0), self.y + (self.height/2.0))
		glVertex2f(self.x + (self.width/2.0), self.y - (self.height/2.0))
		glEnd()



if __name__=='__main__':
	simulation_test = Simulation(9.8, 2)
	print simulation_test
	simulation_test.run()
