#!/usr/bin/python
# filename: rk4.py
# author: latrokles -- latrokles_at_gmail_dot_com
# 

class State:
	def __init__(self):
		self.x = None	#position
		self.v = None	#velocity

class Derivative:
	def __init__(self):
		self.dx = None	#derivative of position: velocity
		self.dv = None	#derivative of velocity: acceleration

def evaluate(initial_state, t, dt, derivative):
	state = State()
	state.x = initial.x + derivative.dx*dt
	state.v = initial.v + derivative.dv*dt

	output = Derivative()
	output.dx = state.v
	output.dv = acceleration(state, t+dt)
	return output

