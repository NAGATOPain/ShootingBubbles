class Scene:

	def __init__(self, display, id, w_size):
		self._is_end = False
		self._display = display
		self._id = id
		self._w_size = w_size

	def update(self):
		pass

	def render(self):
		pass

	def is_end(self):
		return self._is_end

	def id(self):
		return self._id
