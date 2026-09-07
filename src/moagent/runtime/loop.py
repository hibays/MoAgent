from ..runtime.massage import Massage
from ..agent.llm import completion ,tools
from ..tools.builtin import builtin_tools
from .session import Session
from pathlib import Path
import os
import tomllib


def inject_env(env_file=".env"):
	d = tomllib.loads(Path(env_file).read_text("utf-8"))
	for k, v in d.items():
		os.environ[k] = v


def run_loop():
	# 注入环境变量
	inject_env()
	# 给个新对话
	sess = Session()
	# 开始loop
	while True:
		user_input = input(">")
		sess.trace.te(user_input)
		response = completion(
		    model="deepseek-v4-flash",
		    provider="deepseek",
		    messages=sess.mess_cur(),
		    tools=[tools.callable_to_tool(tool) for tool in builtin_tools]
		)
		sess.trace.te(response)
