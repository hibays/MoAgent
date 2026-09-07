from .tool import tool
class ToolRegistry:
	def __init__(self):
		self.tools : dict[str, tool] = {}