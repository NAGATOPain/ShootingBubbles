from src.scene.scene import Scene
from src.element.character import Character
from src.element.burble import Burble
import pygame, os


class GameScene(Scene):
	
	# Constant:
	__FONT = "Arial"
	__FONT_SIZE = 50
	__FONT_COLOR = (136, 0, 100)
	__TIME_INCREASE_BURBLE = 3.0
	__LIMIT_BURBLE = 200

	def __init__(self, display, id, w_size):
		super().__init__(display, id, w_size)
		# Init score label
		self.__font = pygame.font.SysFont(self.__FONT, self.__FONT_SIZE)
		self.__font.set_bold(True)
		self.__score = 0
		# Init game elements
		self.__char = Character(display, w_size)
		self.__burble = []
		self.__MAX_BURBLE = 40
		while len(self.__burble) < self.__MAX_BURBLE:
			self.__burble.append(Burble(display, w_size))

		self.__time = 0.0 # The variable which make MAX_BURBLE increase over time

		# Audio of shooting
		shoot_path = os.path.abspath("res/Shoot.wav")
		self.__shoot_effect = pygame.mixer.Sound(shoot_path)
		# Audio of boom !:
		boom_path = os.path.abspath("res/Explosion.wav")
		self.__boom_effect = pygame.mixer.Sound(boom_path)
		
	def update(self):
		super().update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.__char.set_status("Up")
				elif event.key == pygame.K_DOWN:
					self.__char.set_status("Down")
				elif event.key == pygame.K_LEFT:
					self.__char.set_status("Left")
				elif event.key == pygame.K_RIGHT:
					self.__char.set_status("Right")
				elif event.key == pygame.K_SPACE:
					# Shoot:
					self.__shoot_effect.play()
					self.__char.shoot()

		self.__char.rotate()
		self.__char.move()
		for burble in self.__burble:
			# If burble is out of screen
			if burble.out():
				self.__burble.remove(burble)
			burble.move()
			# Check if Bullet shoot the burbles !:
			for bullet in self.__char.get_bullet():
				if ((bullet.get_pos()[0] - burble.get_pos()[0]) ** 2 + (bullet.get_pos()[1] - burble.get_pos()[1]) ** 2) ** (0.5) <= (bullet.get_r() + burble.get_r()):
					# Bullet got it !
					self.__boom_effect.play()
					# Remove bullet :
					self.__char.get_bullet().remove(bullet)
					self.__score += 1
					if burble.get_level() == 1:
						self.__burble.remove(burble)
					elif burble.get_level() == 2:
						pos = burble.get_pos()
						self.__burble.remove(burble)
						self.__burble.append(Burble(self._display, self._w_size, pos, 1))
						self.__burble.append(Burble(self._display, self._w_size, [pos[0] + 1, pos[1] + 1], 1))
					elif burble.get_level() == 3:
						pos = burble.get_pos()
						self.__burble.remove(burble)
						self.__burble.append(Burble(self._display, self._w_size, pos, 2))
						self.__burble.append(Burble(self._display, self._w_size, [pos[0] + 1, pos[1] + 1], 2))
					else: 
						pass
				else: 
					pass
			# Check if burble get character
			a, b, c = self.__char.get_pointset()
			d_a = ((a[0] - burble.get_pos()[0]) ** 2 + (a[1] - burble.get_pos()[1]) ** 2) ** 0.5
			d_b = ((b[0] - burble.get_pos()[0]) ** 2 + (b[1] - burble.get_pos()[1]) ** 2) ** 0.5
			d_c = ((c[0] - burble.get_pos()[0]) ** 2 + (c[1] - burble.get_pos()[1]) ** 2) ** 0.5
			if d_a <= burble.get_r() or d_b <= burble.get_r() or d_c <= burble.get_r():
				# Character hit the burble ! DIE !
				self._is_end = True
				# Save score to file:
				f = open("data\\lastscore.dat", 'w')
				f.write(str(self.__score))
				f.close()


		# Update for num of burble get to Max number
		while len(self.__burble) < self.__MAX_BURBLE:
			self.__burble.append(Burble(self._display, self._w_size))

		# Make MAX_NUMBER of burbles increase over 2s, but not over limit
		if self.__MAX_BURBLE < self.__LIMIT_BURBLE:
			self.__time += 1.0/60
			if self.__time > self.__TIME_INCREASE_BURBLE: 
				self.__MAX_BURBLE += 1
				self.__time = 0

	def render(self):
		super().render()
		self.__char.render()
		for burble in self.__burble:
			burble.render()
		# Render score label
		score_text = str(self.__score)
		score_lbl = self.__font.render(score_text, True, self.__FONT_COLOR)
		self._display.blit(score_lbl, ((self._w_size[0] - score_lbl.get_width()) // 2, self._w_size[1] // 6 - score_lbl.get_height() // 2))