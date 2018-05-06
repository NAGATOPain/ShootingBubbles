import  pygame
from math import sin, cos, pi
from src.element.bullet import Bullet

# Character is an equilateral triangle
class Character:

	# Constants:
	__COLOR = (255, 255, 0) # Yellow
	__RATIO = 20
	__SPEED_ROTATION = 1.0 / 90
	__SPEED_MOVEMENT = 1.5
	__HEAD_COLOR = (255, 0 ,0) # Red

	def __init__(self, display, w_size):
		self.__display = display
		self.__w_size = w_size
		self.__pos = [w_size[0] // 2, w_size[1] // 2] # Center of Character
		self.__corner = 0;

		# Head:
		self.__head = self.__pos[0] + self.__RATIO * sin(self.__corner), self.__pos[1] - self.__RATIO * cos(self.__corner)

		# Movement:
		self.__status = "static"

		# Bullet:
		self.__bullet = []

	def set_status(self, status):
		self.__status = status

	# Get character's 3 point
	def get_pointset(self):
		a = self.__pos[0] + self.__RATIO * sin(self.__corner), self.__pos[1] - self.__RATIO * cos(self.__corner)
		b = self.__pos[0] + self.__RATIO * sin(self.__corner + 2*pi/3), self.__pos[1] - self.__RATIO * cos(self.__corner+2*pi/3)
		c = self.__pos[0] + self.__RATIO * sin(self.__corner + 4*pi/3), self.__pos[1] - self.__RATIO * cos(self.__corner+4*pi/3)
		self.__head = a # Set the head to point a
		return a,b,c

	def rotate(self):
		self.__corner += pi * self.__SPEED_ROTATION
		if self.__corner >= 2*pi:
			self.__corner -= 2*pi

	# Get bullet pos:
	def get_bullet(self):
		return self.__bullet

	def shoot(self):
		self.__bullet.append(Bullet(self.__display, self.__w_size, self.__pos, self.__head))

	def move(self):
		# Make sure that character not go out screen
		if self.__pos[0] < -self.__RATIO:
			self.__pos[0] += (self.__w_size[0] + 2*self.__RATIO)
		elif self.__pos[0] > self.__RATIO + self.__w_size[0]:
			self.__pos[0] -= (self.__w_size[0] + self.__RATIO * 2)
		if self.__pos[1] < -self.__RATIO:
			self.__pos[1] += (self.__w_size[1] + 2*self.__RATIO)
		elif self.__pos[1] > self.__RATIO + self.__w_size[1]:
			self.__pos[1] -= (self.__w_size[1] + self.__RATIO * 2)
		# Movement:
		if self.__status == "Up":
			self.__pos[1] -= self.__SPEED_MOVEMENT
		elif self.__status == "Down":
			self.__pos[1] += self.__SPEED_MOVEMENT
		elif self.__status == "Left":
			self.__pos[0] -= self.__SPEED_MOVEMENT
		elif self.__status == "Right": 
			self.__pos[0] += self.__SPEED_MOVEMENT
		else:
			pass

		# Move bullet:
		for bullet in self.__bullet:
			if bullet.is_out():
				# The bullet is out of the screen
				self.__bullet.remove(bullet)
			bullet.move()

	def render(self): 
		pygame.draw.polygon(self.__display, self.__COLOR, self.get_pointset())
		pygame.draw.circle(self.__display, self.__HEAD_COLOR, (int(self.__head[0]), int (self.__head[1])), 2)
		for bullet in self.__bullet:
			bullet.render()
