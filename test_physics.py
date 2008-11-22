#!/usr/bin/python
# filename: physics_test.py
# author: latrokles 
#
# description: Tests for the particle physics engine in physics.py. This
# also reflects how the system may be used in an actual program.
#

from pyglet.gl import *
from pyglet import window
import physics

class Visualization:
	"""A visualization window to see how the particles are created
	and how they interact with each other"""
	def __init__(self, caption):
		self.main_window     = window.Window(caption=caption)
		self.particle_system = physics.ParticleSystem()
	
	def draw_particles(self, x, y):
		"""Draw squares for each particle"""
		width, height = 10, 10
		glBegin(GL_QUADS)
		glVertex2f(x - (width/2.0), y - (height/2.0))
		glVertex2f(x - (width/2.0), y + (height/2.0))
		glVertex2f(x + (width/2.0), y + (height/2.0))
		glVertex2f(x + (width/2.0), y - (height/2.0))
		glEnd()
