from typing import Callable
from dataclasses import dataclass

@dataclass
class tool:
	name: str
	description: str
	func: Callable
	args_schema: dict|None = None