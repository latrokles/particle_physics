#!/usr/bin/python
# filename: physics.py
# author: latrokles - latrokles_at_gmail_com
#
# description: Describes a simple particle system that includes
# springs and forces.
class Vector:
	"""A VERY SIMPLE Vector class"""
	def __init__(self, data):
		self.data = data

	def __repr__(self):
		return repr(self.data)
	
	def __add__(self, other):
		data = []
		for index in range(len(self.data)):
			data.append(self.data[index] + other.data[index])
		return Vector(data)

	def __getitem__(self, index):
		return self.data[index]

	def __setitem__(self, indexi, value):
		self.data[index] = value
	
	def pop(self):
		return self.data.pop(0)
	
	#Should this be mutable or not???, for now I guess it will be
	def scale(self, scale_factor):
		self.data = [ x * scale_factor for x in self.data]

class Particle:
	def __init__(self, mass, x=0, y=0, z=0):
		self.mass = mass
		self.position_vector = Vector([x,y,z])
		self.velocity_vector = Vector([0,0,0])
		self.force_accumulator = None	#not implemented yet
	
	def __repr__(self):
		print "Particle at", self.position_vector


class ParticleSystem:
	def __init__(self, gravity=0.0, drag=0.0):
		self.gravity   = gravity
		self.drag      = drag
		self.particles = []
		self.simulation_clock = 0.0

	def __repr__(self):
		print "Particle System"
		print "(Gravity:%f, Drag:%f)" % self.gravity, self.drag
		for particle in self.particles:
			print particle
	
	### Interactive stuff ###
	def make_particle(self, mass, x, y, z):
		"""x.make_particle(mass, x, y, z) --> Particle --- Creates a new 
		particle in the system with some mass and x,y,z coordinates"""
		temp_particle = Particle(mass, x, y, z)
		self.particles.append(temp_particle)
		return temp_particle

	def get_particle(self, index):
		"""x.get_particle(index) --> Particle --- Gets particle at index"""
		return self.particles[index]

	def number_of_particles(self):
		"""x.number_of_particles() --> int --- Returns the number of 
		particles in the particle system"""
		return len(self.particles)

	def clear(self):
		"""x.clear() --> None --- Clears all particles in the system"""
		self.particles = []

	def clear_forces(self):
		raise NotImplementedError

	def compute_forces(self):
		raise NotImplementedError

	### ODE Solver ###
	#Length of state derivative, and force vectors
	def particle_dimensions(self):
		return (6 * self.number_of_particles)

	#Gather state from the particles into dst 
	def particle_get_state(self):
		dst = []
		for particle in self.particles:
			dst.append(particle.position_vector[0])
			dst.append(particle.position_vector[1])
			dst.append(particle.position_vector[2])

			dst.append(particle.velocity_vector[0])
			dst.append(particle.velocity_vector[1])
			dst.append(particle.velocity_vector[2])
		return Vector(dst)

	#Scatter state from src into the particles
	def particle_set_state(self, src):
		for particle in self.particles:
			particle.position_vector[0] = src.pop()
			particle.position_vector[1] = src.pop()
			particle.position_vector[2] = src.pop()

			particle.velocity_vector[0] = src.pop()
			particle.velocity_vector[1] = src.pop()
			particle.velocity_vector[2] = src.pop()
	
	#Calculate derivative and place it in dst
	def particle_derivative(self):
		dst = []
		self.clear_forces()
		self.compute_forces()
		for particle in self.particles:
			# xdot = v
			dst.append(particle.velocity_vector[0])
			dst.append(particle.velocity_vector[1])
			dst.append(particle.velocity_vector[2])

			# vdot = f/m
			dst.append(particle.force_accumulator[0]/particle.mass)
			dst.append(particle.force_accumulator[1]/particle.mass)
			dst.append(particle.force_accumulator[2]/particle.mass)
		return Vector(dst)

	#perform euler step
	def euler_step(self, dt):
		temp1 = self.particle_derivative()
		temp1.scale(dt)
		temp2 = self.particle_get_state()
		temp3 = temp1 + temp2
		self.particle_set_state(temp3)
		self.simulation_clock += dt


