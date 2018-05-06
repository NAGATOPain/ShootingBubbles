import pygame, random


class Burble:
	# Burble has 3 level: 1, 2, 3. Level 3 has its size biggest, and level 1 has its size smallest
	# If shoot in a burble which has level > 1 then its level decrease by 1
	# If shoot in a burble which has level = 1 then it disappear

	# Constants:
	__COLOR = (255, 255, 255)
	__WIDTH = 3
	__RATIO_LV_1, __RATIO_LV_2, __RATIO_LV_3 = 10, 20, 40
	__SPEED = 2.0
	__RANGE = 100.0 # The range of screen that burble is in

	def __init__(self, display, w_size, former_pos = None, level = None):
		self.__display = display
		self.__w_size = w_size

		if level is None:
			# Create an level:
			self.__level = random.randint(1,3)
		else:
			self.__level = level

		if former_pos is None:
			# Create an burble:
			dir = random.randint(1,4) # 1 is up, 2 is down, 3 is left, 4 is right of the screen
			if dir == 1: self.__pos = [w_size[0] / 2, -self.__RANGE / 2]
			elif dir == 2: self.__pos = [w_size[0] / 2, w_size[1] + self.__RANGE / 2]
			elif dir == 3: self.__pos = [-self.__RANGE / 2, w_size[1] / 2]
			elif dir == 4: self.__pos = [w_size[1] + self.__RANGE / 2, w_size[1] / 2]
			else:
				pass
		else: self.__pos = former_pos

		# Set up vector of movement
		self.__a = random.uniform(-1,1)
		self.__b = random.uniform(-1,1)

		# Set a variable check whether burble is out of screen
		self.__is_out = False

	def out(self):
		return self.__is_out

	def get_pos(self):
		# Get pos of center:
		return self.__pos

	def get_r(self):
		# Get r of center:
		if self.__level == 1: return self.__RATIO_LV_1
		elif self.__level == 2: return self.__RATIO_LV_2			
		elif self.__level == 3: return self.__RATIO_LV_3
		else: return 0

	def get_level(self):
		return self.__level
			
	def move(self):
		if self.__pos[0] < -self.__RANGE or self.__pos[0] > self.__w_size[0] + self.__RANGE:
			self.__is_out = True
		if self.__pos[1] < -self.__RANGE or self.__pos[1] > self.__w_size[1] + self.__RANGE:
			self.__is_out = True

		self.__pos[0] += self.__a * self.__SPEED
		self.__pos[1] += self.__b * self.__SPEED		

	def render(self):
		if self.__level == 1:
			pygame.draw.circle(self.__display, self.__COLOR, (int(self.__pos[0]), int(self.__pos[1])), self.__RATIO_LV_1, self.__WIDTH)
		elif self.__level == 2:
			pygame.draw.circle(self.__display, self.__COLOR, (int(self.__pos[0]), int(self.__pos[1])), self.__RATIO_LV_2, self.__WIDTH)
		elif self.__level == 3:
			pygame.draw.circle(self.__display, self.__COLOR, (int(self.__pos[0]), int(self.__pos[1])), self.__RATIO_LV_3, self.__WIDTH)
		else:
			pass
