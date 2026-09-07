class ImageMessage:
	__slots__ = ["data"]

	def __init__(self) -> None:
		pass


class TextMessage:
	__slots__ = ["role", "content", "think", "tool_calls", "tool_call_id"]

	def __init__(self) -> None:
		pass


class Massage:
	__slots__ = ["content"]

	def __init__(self) -> None:
		pass
