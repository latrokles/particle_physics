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
    def __init__(self, title):
        self.main_window     = window.Window(caption=title)
        self.particle_system = physics.ParticleSystem()

        #register our even_handlers
        self.main_window.on_mouse_press = self.on_mouse_press
        self.main_window.on_key_press   = self.on_key_press
    
    ### Event Handlers ###
    def on_mouse_press(self, x, y, button, modifiers):
        # make a particle, discard the returned particle, we don't
        # need it in this instance, an application could use the
        # returned particle to keep track of it outside of the 
        # particle system itself (keeping track of the particles
        # composing a simulated cloth sheet comes to mind now).
        self.particle_system.make_particle(5.0, x, y, 0)
        #print "Number of particles = %d" % (self.particle_system.number_of_particles(),)

    def on_key_press(self, symbol, modifiers):
        #space clears the particle system
        if symbol == window.key.SPACE:
            self.particle_system.clear()
        elif symbol == window.key.ESCAPE:
            self.main_window.has_exit = True
    
    ### Visualization Methods ###
    def draw_particles(self):
        for index in range(self.particle_system.number_of_particles()):
            x, y, z = self.particle_system.get_particle(index).get_position()
            self.draw_rect(x, y, 10, 10)

    def draw_rect(self, x, y, w, h):
        """Draw a rectangle at x, y with width w and height h"""
        glBegin(GL_QUADS)
        glVertex2f(x - (w/2.0), y - (h/2.0))
        glVertex2f(x - (w/2.0), y + (h/2.0))
        glVertex2f(x + (w/2.0), y + (h/2.0))
        glVertex2f(x + (w/2.0), y - (h/2.0))
        glEnd()

    def run(self):
        while not self.main_window.has_exit:
            self.main_window.dispatch_events()
            glClear(GL_COLOR_BUFFER_BIT)
            glLoadIdentity()

            self.draw_particles()

            self.main_window.flip()

#### Test routines in here ####
def test_particles_only():
    simulation = Visualization('Only Particles')
    simulation.run()


if __name__=='__main__':
    test_particles_only()
