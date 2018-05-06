from src.scene.scene import Scene
import pygame, os


class EndScene(Scene):
	
	# Constants:
	
	__FONT = "Arial"
	__FONT_COLOR = (255, 255, 255)
	__FONT_TITLE_SIZE = 50
	__FONT_SCORE_SIZE = 30
	__TITLE = "GAME OVER"

	def __init__(self, display, id, w_size):
		super().__init__(display, id, w_size)

		score_lbl = "Score: "
		highscore_lbl = "High Score: "

		# Read file
		f = open("data\\lastscore.dat", "r")
		last_score = int(f.read())
		f.close()

		f_1 = open("data\\highscore.dat", "r")
		high_score = int(f_1.read())
		f_1.close()
		f_2 = open("data\\highscore.dat", "w")
		if last_score > high_score: high_score = last_score
		f_2.write(str(high_score))
		f_2.close()

		score_lbl += str(last_score)
		highscore_lbl += str(high_score)

		# Init font:
		font_title = pygame.font.SysFont(self.__FONT, self.__FONT_TITLE_SIZE)
		font_title.set_bold(True)
		self.__title_lbl = font_title.render(self.__TITLE, True, self.__FONT_COLOR)

		font_score = pygame.font.SysFont(self.__FONT, self.__FONT_SCORE_SIZE)
		font_score.set_bold(False)
		self.__score_lbl = font_score.render(score_lbl, True, self.__FONT_COLOR)

		font_h_score = pygame.font.SysFont(self.__FONT, self.__FONT_SCORE_SIZE)
		font_h_score.set_bold(False)
		self.__h_score_lbl = font_h_score.render(highscore_lbl, True, self.__FONT_COLOR)

		# Audio of die
		die_path = os.path.abspath("res/Die.wav")
		self.__die_effect = pygame.mixer.Sound(die_path)
		self.__die_effect.play()

	def update(self):
		super().update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self._is_end = True
				else: pass
			else: pass

	def render(self):
		super().render()
		self._display.blit(self.__title_lbl,\
							(self._w_size[0] // 2 - self.__title_lbl.get_width() // 2,\
							int(self._w_size[1] // 2.5) - self.__title_lbl.get_height() // 2))
		self._display.blit(self.__score_lbl,\
							(self._w_size[0] // 2 - self.__score_lbl.get_width() // 2,\
							int(self._w_size[1] // 1.75) - self.__score_lbl.get_height() // 2))
		self._display.blit(self.__h_score_lbl,\
							(self._w_size[0] // 2 - self.__h_score_lbl.get_width() // 2,\
							int(self._w_size[1] / 1.6) - self.__h_score_lbl.get_height() // 2))