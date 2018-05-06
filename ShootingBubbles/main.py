import pygame
from src.scene.scenemanager import SceneManager
from src.scene.titlescene import TitleScene
from src.scene.gamescene import GameScene
from src.scene.endscene import EndScene

pygame.init()
pygame.font.init()

# Game Constants:

SIZE = WIDTH, HEIGHT = 700, 700
BACKGROUND_COLOR = (0, 0, 0)

# Set game's basic attributes:

display = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Shooting Bubbles - NTL")

# Game variables:
gsm = SceneManager()
gsm.set_scene(TitleScene(display, 1, SIZE)) # Title Scene

while True:

	pygame.time.delay(1000 // 60) # FPS = 60
	display.fill(BACKGROUND_COLOR)
	if gsm.get_scene().is_end():
		if gsm.get_scene().id() == 1:
			gsm.set_scene(GameScene(display, 2, SIZE))
		elif gsm.get_scene().id() == 2:
			gsm.set_scene(EndScene(display, 3, SIZE))
		elif gsm.get_scene().id() == 3:
			gsm.set_scene(TitleScene(display, 1, SIZE))
		else:
			pass
	else: pass
	gsm.get_scene().update()
	gsm.get_scene().render()
	pygame.display.update()