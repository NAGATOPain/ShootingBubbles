from src.scene.scene import Scene
from src.element.character import Character
from src.element.bubble import Bubble
import pygame, os, sys


class GameScene(Scene):
	
	# Constant:
	__FONT = "Arial"
	__FONT_SIZE = 50
	__FONT_COLOR = (136, 0, 100)
	__TIME_INCREASE_BUBBLE = 3.0
	__LIMIT_BUBBLE = 200

	def __init__(self, display, id, w_size):
		super().__init__(display, id, w_size)
		# Init score label
		self.__font = pygame.font.SysFont(self.__FONT, self.__FONT_SIZE)
		self.__font.set_bold(True)
		self.__score = 0
		# Init game elements
		self.__char = Character(display, w_size)
		self.__bubble = []
		self.__MAX_BUBBLE = 40
		while len(self.__bubble) < self.__MAX_BUBBLE:
			self.__bubble.append(Bubble(display, w_size))

		self.__time = 0.0 # The variable which make MAX_BUBBLE increase over time

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
				sys.exit()
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
		for bubble in self.__bubble:
			# If bubble is out of screen
			if bubble.out():
				self.__bubble.remove(bubble)
			bubble.move()
			# Check if Bullet shoot the bubbles !:
			for bullet in self.__char.get_bullet():
				if ((bullet.get_pos()[0] - bubble.get_pos()[0]) ** 2 + (bullet.get_pos()[1] - bubble.get_pos()[1]) ** 2) ** (0.5) <= (bullet.get_r() + bubble.get_r()):
					# Bullet got it !
					self.__boom_effect.play()
					# Remove bullet :
					self.__char.get_bullet().remove(bullet)
					self.__score += 1
					if bubble.get_level() == 1:
						self.__bubble.remove(bubble)
					elif bubble.get_level() == 2:
						pos = bubble.get_pos()
						self.__bubble.remove(bubble)
						self.__bubble.append(Bubble(self._display, self._w_size, pos, 1))
						self.__bubble.append(Bubble(self._display, self._w_size, [pos[0] + 1, pos[1] + 1], 1))
					elif bubble.get_level() == 3:
						pos = bubble.get_pos()
						self.__bubble.remove(bubble)
						self.__bubble.append(Bubble(self._display, self._w_size, pos, 2))
						self.__bubble.append(Bubble(self._display, self._w_size, [pos[0] + 1, pos[1] + 1], 2))
					else: 
						pass
				else: 
					pass
			# Check if bubble get character
			a, b, c = self.__char.get_pointset()
			d_a = ((a[0] - bubble.get_pos()[0]) ** 2 + (a[1] - bubble.get_pos()[1]) ** 2) ** 0.5
			d_b = ((b[0] - bubble.get_pos()[0]) ** 2 + (b[1] - bubble.get_pos()[1]) ** 2) ** 0.5
			d_c = ((c[0] - bubble.get_pos()[0]) ** 2 + (c[1] - bubble.get_pos()[1]) ** 2) ** 0.5
			if d_a <= bubble.get_r() or d_b <= bubble.get_r() or d_c <= bubble.get_r():
				# Character hit the bubble ! DIE !
				self._is_end = True
				# Save score to file:
				f = open("data\\lastscore.dat", 'w')
				f.write(str(self.__score))
				f.close()


		# Update for num of bubble get to Max number
		while len(self.__bubble) < self.__MAX_BUBBLE:
			self.__bubble.append(Bubble(self._display, self._w_size))

		# Make MAX_NUMBER of bubbles increase over 2s, but not over limit
		if self.__MAX_BUBBLE < self.__LIMIT_BUBBLE:
			self.__time += 1.0/60
			if self.__time > self.__TIME_INCREASE_BUBBLE: 
				self.__MAX_BUBBLE += 1
				self.__time = 0

	def render(self):
		super().render()
		self.__char.render()
		for bubble in self.__bubble:
			bubble.render()
		# Render score label
		score_text = str(self.__score)
		score_lbl = self.__font.render(score_text, True, self.__FONT_COLOR)
		self._display.blit(score_lbl, ((self._w_size[0] - score_lbl.get_width()) // 2, self._w_size[1] // 6 - score_lbl.get_height() // 2))