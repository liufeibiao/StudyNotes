# from typing import overload
#
#
# @overload
# def test_a(a: int, ) -> tuple: ...
#
#
# # @overload
# # def test_a(a: str, b: dict, ) -> list: ...
#
#
# def test_a(a, b, ):
# 	print(type(a), a, type(b), b)
#
#
# test_a("ss", {})
from typing import overload, Union, Dict, List, Tuple


# 重载签名
@overload
def test_a(a: int) -> Tuple[int]: ...


@overload
def test_a(a: str, b: Dict) -> List[str]: ...


# 实际实现
def test_a(a: Union[int, str], b: Dict = None) -> Union[List[str], Tuple[int]]:
	if isinstance(a, int):
		return (a,)
	elif isinstance(a, str) and isinstance(b, dict):
		return [a, b]
	else:
		raise TypeError("Invalid arguments")


# 调用实际实现
print(test_a(10))  # 输出: (10,) .直接调用tuple的函数
print(test_a("ss", {}))  # 输出: ['ss',{}] .直接调用list的函数
