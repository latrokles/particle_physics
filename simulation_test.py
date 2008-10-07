#!/usr/bin/python
# filename: simulation_test.py
# author: Latrokles -- latrokles@samuraihippo.com
# 
# description:
# A simulation of a simple particle physics using python and pyglet
from pyglet.gl import *
from pyglet import window

class Simulation:
	def __init__(self, grav):
		self.rigid_bodies = []
		self.main_window = window.Window(caption="Simulation")
		self.override_functions()
		self.gravity = grav

	def override_functions(self):
		#self.main_window.on_mouse_motion = self.on_mouse_motion
		self.main_window.on_mouse_press = self.on_mouse_press
	
	def insert_body(self, body):
		self.rigid_bodies.append(body)
	
	def on_mouse_press(self, x, y, button, modifiers):
		self.insert_body(Rectangle(x, y, 10, 10))

	def on_mouse_motion(self, x, y, dx, dy):
		print "Mouse coordinates: (%d, %d)" % (x, y)
	
	def draw_bodies(self):
		for body in self.rigid_bodies:
			body.draw()
	
	def update_bodies(self):
		for body in self.rigid_bodies:
			body_coordinates == body.get_coordinates()
			if body_coordinates[0] <= 0:
				pass
			body.update_position(0, self.gravity)
	
	def run(self):
		while not self.main_window.has_exit:
			self.main_window.dispatch_events()
			glClear(GL_COLOR_BUFFER_BIT)
			glLoadIdentity()

			self.draw_bodies()
			self.update_bodies()

			self.main_window.flip()

class rigid_body:
	def __init__(self):
		pass
	
	def update_position(self, dx, dy):
		raise NotImplementedError
	
	def draw(self):
		raise NotImplementedError

	def update(self):
		raise NotImplementedError

class Rectangle:
	def __init__(self, x, y, w, h):
		self.x_position = x
		self.y_position = y
		self.height = h
		self.width = w
	
	def draw(self):
		glBegin(GL_QUADS)
		glVertex2f(self.x_position, self.y_position)
		glVertex2f(self.x_position, self.y_position + self.height)
		glVertex2f(self.x_position + self.width, self.y_position + self.height)
		glVertex2f(self.x_position + self.width, self.y_position)
		glEnd()

	def update_coordinates(self, dx, dy):
		self.x_position += dx
		self.y_position += dy
	
	def get_coordinates(self):
		return (self.x_position, self.y_position)


def main():
	"""Program's main method"""
	Simulation(-9.8).run()

if __name__=='__main__':
	main()
