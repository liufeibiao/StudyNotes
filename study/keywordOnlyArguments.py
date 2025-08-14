def positional_only_demo(a: int, b: int, /, c: int, d: int = 0) -> int:
	"""
	说明:
		演示“位置仅限参数”（positional-only），使用 `/` 分隔。
		- `/` 之前的 a, b 只能用位置传参；
		- `/` 之后、`*` 之前的 c, d 可位置或关键字传参。

	示例:
		positional_only_demo(1, 2, 3)            -> 正确
		positional_only_demo(a=1, b=2, c=3)      -> 错误，a/b 不能用关键字
	"""
	return a + b + c + d
	# 6) 位置仅限参数：a、b 只能位置传参
print(positional_only_demo(1, 2, 3))

def mixed_signature(a: int, /, b: int, *args: int, c: int, d: int = 0, **kwargs) -> dict:
	"""
	说明:
		综合示例，涵盖 `/`, `*args`, 关键字仅限 `c`/`d`，以及 `**kwargs`。
		- a: 位置仅限
		- b: 位置或关键字均可
		- *args: 额外的位置参数
		- c, d: 关键字仅限
		- **kwargs: 额外的关键字参数

	示例:
		mixed_signature(1, 2, 3, 4, c=5, d=6, x=7)
	"""
	return {
		"a": a,
		"b": b,
		"args": args,
		"c": c,
		"d": d,
		"kwargs": kwargs,
	}


def mutable_default_bad(xs: list = []):
	"""
	说明:
		演示“可变默认参数”的陷阱：默认值在函数定义时只计算一次，会被所有调用共享。
	"""
	xs.append(1)
	return xs


def mutable_default_good(xs: list | None = None):
	"""
	说明:
		正确做法：使用 None 作为默认值，再在函数体内创建新列表，避免共享同一个列表。
	"""
	if xs is None:
		xs = []
	xs.append(1)
	return xs


def order_rule_demo():
	"""
	记忆模板（不执行，仅文档目的）：

	def func(pos_only1, pos_only2, /,
	         pos_or_kw1, pos_or_kw2,
	         *,
	         kw_only1, kw_only2,
	         **kwargs):
		...

	顺序规则：
		位置仅限 -> 斜杠 / -> 位置或关键字 -> 星号 * -> 关键字仅限 -> **kwargs
	"""
	pass


if __name__ == '__main__':

      # 正确 -> 1+2+3=6
	# print(positional_only_demo(a=1, b=2, c=3)) # 错误示例：a、b 不可关键字

	# 7) 综合签名：包含 /, *args, 关键字仅限, **kwargs
	print(mixed_signature(1, 2, 3, 4, c=5, d=6, x=7))

	# 8) 可变默认参数陷阱与修复
	print(mutable_default_bad())   # 第一次 -> [1]
	print(mutable_default_bad())   # 第二次 -> [1, 1]  累积了！
	print(mutable_default_good())  # 每次 -> [1]
