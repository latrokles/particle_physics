#!/usr/bin/python
# filename: physics.py
# author: latrokles - latrokles_at_gmail_com
#
# description: Describes a simple particle system that includes
# springs and forces.

class Particle:
	def __init__(self, mass, position)
		self.mass = mass
		self.position_vector = position
		self.velocity_vector = None
		self.force_accumulator = None
	
	def __repr__(self):
		print "Particle at", self.position_vector


class ParticleSystem:
	def __init__(self, gravity=0.0, drag=0.0):
		self.gravity   = gravity
		self.drag      = drag
		self.particles = []
		self.number_of_particles = 0
		self.simulation_clock = 0.0

	def __repr__(self):
		print "Particle System"
		print "(Gravity:%f, Drag:%f)" % self.gravity, self.drag
		for particle in self.particles:
			print particle
	
	def calculate_forces(self):
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
		return dst

	#Scatter state from src into the particles
	def particle_set_state(self, src):
		for particle in self.particles:
			particle.position_vector[0] = src.pop(0)
			particle.position_vector[1] = src.pop(0)
			particle.position_vector[2] = src.pop(0)

			particle.velocity_vector[0] = src.pop(0)
			particle.velocity_vector[1] = src.pop(0)
			particle.velocity_vector[2] = src.pop(0)
	
	#Calculate derivative and place it in dst
	def particle_derivatice(self):
		dst = []
		self.clear_forces()
		self.compute_forces()
		for particle in self.particles:
			# xdot = v
			dst.append(particle.velocity_vector[0])
			dst.append(particle.velocity_vector[1])
			dst.append(particle.velocity_vector[2])

			dst.append(particle.force_accumulator[0]/particle.mass)
			dst.append(particle.force_accumulator[1]/particle.mass)
			dst.append(particle.force_accumulator[2]/particle.mass)
		return dst

