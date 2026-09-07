from .trace import Trace

import uuid


class Session:
	__slots__ = ["sid", "trace"]

	def __init__(self, sid_recovery=None):
		if sid_recovery is None:
			self.sid = uuid.uuid4()
		else:
			# TODO
			...
		self.trace = Trace()

	def mess_cur(self):
		...

	def dumps(self) -> bytes:
		...

	def save(self, target):
		...

	def load(self, data):
		...
