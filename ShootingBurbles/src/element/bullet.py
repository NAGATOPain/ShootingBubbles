import pygame

class Bullet():

	# Constants:
	__MOVEMENT_SPEED = 0.2
	__RATIO = 2
	__COLOR = (255, 0 ,0) # Red

	def __init__(self, display, w_size, center, point):
		self.__display = display
		self.__w_size = w_size
		self.__point = point

		# The equaltion is x = x0 + at, y = y0 + bt with x is increase or decrease
		x0, y0, u0, t0 = center[0], center[1], point[0], point[1]
		# Vector of movement vct = (a,b)
		self.__a = u0 - x0
		self.__b = t0 - y0

		# Init the very first position
		self.__pos = [u0, t0]
		self.__t = 0

		# The variable show that whether the bullet is out of screen
		self.__out = False

	def move(self):
		self.__t += self.__MOVEMENT_SPEED
		self.__pos[0] = self.__point[0] + self.__a * self.__t
		self.__pos[1] = self.__point[1] + self.__b * self.__t
		if self.__pos[0] <= -self.__RATIO or self.__pos[0] >= self.__w_size[0] + self.__RATIO:
			self.__out = True
		if self.__pos[1] <= -self.__RATIO or self.__pos[1] >= self.__w_size[1] + self.__RATIO:
			self.__out = True

	def is_out(self):
		return self.__out

	def get_pos(self):
		return self.__pos

	def get_r(self):
		return self.__RATIO

	def render(self):
		pygame.draw.circle(self.__display, self.__COLOR, (int(self.__pos[0]), int(self.__pos[1])), self.__RATIO)
