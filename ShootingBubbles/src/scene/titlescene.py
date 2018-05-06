from src.scene.scene import Scene
import pygame, sys

class TitleScene(Scene):

	# Constants:
	
	__FONT = "Arial"
	__FONT_COLOR = (255, 255, 255)
	__FONT_TITLE_SIZE = 50
	__FONT_TUT_SIZE = 30
	__TITLE = "SHOOTING BUBBLES"
	__TUT = "Space to Play !"

	def __init__(self, display, id, w_size):
		super().__init__(display, id, w_size)

		# Init font:
		font_title = pygame.font.SysFont(self.__FONT, self.__FONT_TITLE_SIZE)
		font_title.set_bold(True)
		self.__title_lbl = font_title.render(self.__TITLE, True, self.__FONT_COLOR)

		font_tut = pygame.font.SysFont(self.__FONT, self.__FONT_TUT_SIZE)
		font_tut.set_bold(False)
		self.__tut_lbl = font_tut.render(self.__TUT, True, self.__FONT_COLOR)


	def update(self):
		super().update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self._is_end = True
				else: pass
			else: pass

	def render(self):
		super().render()
		self._display.blit(self.__title_lbl,\
							(self._w_size[0] // 2 - self.__title_lbl.get_width() // 2,\
							self._w_size[1] // 3 - self.__title_lbl.get_height() // 2))
		self._display.blit(self.__tut_lbl,\
							(self._w_size[0] // 2 - self.__tut_lbl.get_width() // 2,\
							self._w_size[1] // 2 - self.__tut_lbl.get_height() // 2))