class Trace:
	__slots__ = ["stack"]

	def __init__(self):
		self.stack = []

	def te(self, obj):
		self.stack.append(obj)