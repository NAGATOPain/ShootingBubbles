class SceneManager:

	def __init__(self):
		self.__scene_manager = []

	def set_scene(self, scene):
		if len(self.__scene_manager) > 0:
			self.__scene_manager.pop()
			self.__scene_manager.append(scene)
		else:
			self.__scene_manager.append(scene)

	def get_scene(self):
		return self.__scene_manager[0]
