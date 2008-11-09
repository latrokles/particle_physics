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

		#variables to keep track of particle being created
		self.current_x = 0
		self.current_y = 0
		self.previous_x = 0
		self.previous_y = 0
		self.temp_particle = None
		#End of temporary particle variables

		self.bounds = self.set_bounds()
		self.window.on_mouse_press   = self.on_mouse_press
		self.window.on_mouse_release = self.on_mouse_release
		self.window.on_mouse_drag    = self.on_mouse_drag
		self.window.on_draw          = self.on_draw

	def __repr__(self):
		return 'Simulation parameters:\nGravity:\t%d\nDrag:\t\t%d' % (self.gravity, self.drag)

	def set_bounds(self):
		width, height = self.window.get_size()
		return {'LEFT':0, 'RIGHT':width, 'BOTTOM':0, 'TOP':height }

	#Event Handlers for pyglet window
	def on_mouse_press(self, x, y, button, modifiers):
		self.temp_particle = Rectangle(x, y, 0, 0, 10, 10)
		self.current_x, self.current_y = self.previous_x, self.previous_y = x, y
		self.particles.append(self.temp_particle)
	
	def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
		self.current_x = x
		self.current_y = y
	
	def on_mouse_release(self, x, y, button, modifiers):
		dx = (self.previous_x - self.current_x) * 0.05
		dy = (self.previous_y - self.current_y) * 0.05
		self.temp_particle.set_velocity(dx, dy)
		self.clear_velocity_data()

	def on_mouse_motion(self, x, y, dx, dy):
		raise NotImpplementedError
		#print '(%d, %d):' % (self.temp_dx, self.temp_dy)
	#End of Event Handlers

	def draw_spring_line(self):
		glBegin(GL_LINES)
		glVertex2f(self.current_x, self.current_y)
		glVertex2f(self.previous_x, self.previous_y)
		glEnd()

	def clear_velocity_data(self):
		self.current_x = 0
		self.current_y = 0
		self.previous_y = 0
		self.previous_y = 0
		self.temp_particle = None

	def update_particles(self):
		"""Updates the position of every particle in the simulation"""
		for particle in self.particles:
			particle.update_coordinates(self.bounds)

	def draw_particles(self):
		"""Draws all particles in the simulation"""
		for particle in self.particles:
			particle.draw()

	def run(self):
		while not self.window.has_exit:
			self.window.dispatch_events()
			glClear(GL_COLOR_BUFFER_BIT)
			glLoadIdentity()
			self.update_particles()
			if self.temp_particle != None:
				self.draw_spring_line()
			self.draw_particles()
			self.window.flip()

	def on_draw(self):
		self.window.clear()
		self.update_particles()
		self.draw_particles()

class Particle:
	"""Defines a single particle, either 2D or 3D"""
	def __init__(self, x=0, y=0, dx=0, dy=0):
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy

	def is_out_of_bounds(self, bounds):
		raise NotImplementedError

	def get_coordinates(self):
		return (self.x, self.y)

	def set_velocity(self, dx, dy):
		self.dx = dx
		self.dy = dy

	def update_coordinates(self, bounds):
		self.x += self.dx
		self.y += self.dy

	def draw(self):
		raise NotImplementedError

class Rectangle(Particle):
	def __init__(self, x=0, y=0, dx=0, dy=0, w=0, h=0):
		Particle.__init__(self, x, y, dx, dy)
		self.width  = w
		self.height = h
	
	def is_out_bounds(self, bounds):
		#if a particle hits a bound, we just reverse the direction of dx, this works for both directions
		#in the same way and it's pretty straightforward... I think
		if (self.x - self.width/2.0) <= bounds['LEFT'] or (self.x + self.width/2.0) >= bounds['RIGHT']:
			self.dx = -self.dx

		if (self.y - self.height/2.0) <= bounds['BOTTOM'] or (self.y + self.height/2.0) >= bounds['TOP']:
			self.dy = -self.dy


	def update_coordinates(self, bounds):
		#bounds is a dictionary with the boundaries of the simulation window, we pass this dict to 
		#is_out_of_bounds to do the necessary changes to the dx and dy of the particle in question
		#I'm using rectangles now, so some of this may be handled differently in other particles, don't 
		#know yet
		self.is_out_bounds(bounds)
		self.x += self.dx
		self.y += self.dy
	
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
	#pyglet.app.run()
