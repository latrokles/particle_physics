#!/usr/bin/python
# filename: physics.py
# author: latrokles 
#
# description: Describes a simple particle system that includes
# springs and forces. It is modeled after the one described by
# Andrew Witkin in his paper "Physically Based Modeling Particle
# System Dynamics". I am using Glenn Fiedler articles on game 
# physics as well.
#

class Vector:
    """Simple 2D Vector class"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other_vector):
        result = Vector()
        result.x = self.x + other_vector.x
        result.y = self.y + other_vector.y
        return result

    def __mult__(self, scalar):
        result = Vector()
        result.x = self.x * scalar
        resutl.y = self.y * scalar
        return result

class Particle:
    """Defines the state of a particle"""
    def __init__(self, m, x, y):
        self.position = Vector(x, y)
        self.velocity = None
        self.momentum = None

        self.mass = m
        self.inverse_mass = None
    
    def recalculate(self):
        self.velocity = momentum * inverse_mass

class Derivative:
    """Derivative to be used in the integrarion."""
    def __init__(self):
        self.dx = None	#derivative of position: velocity
        self.dv = None  #derivative of velocity: acceleration

class ParticleSystem:
    """Particle Physisc System using an RK4 Integrator."""
    def __init__(self, g=0.0, d=0.0):
        self.gravity   = g
        self.drag      = 0
        self.particles = []
        self.forces    = []

    ## Interactive Functions ##
    def make_particle(self, m, x, y, z):
        """Creates a particle with mass m, at coordinates y, y, z."""
        pass

    def number_of_particles(self):
        return len(self.particles)

    def number_of_forces(self):
        return len(self.forces)

    def clear_system(self):
        """Clears particles, forces, and any other accumulators in the system,
        resets system to initial state."""
        self.particles = []
        self.forces    = []
    
    ## End Interactive Functions ##
