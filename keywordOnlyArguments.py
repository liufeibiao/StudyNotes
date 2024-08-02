# **********************************************************************************************
# ***											关键字参数*学习									   			    ***
# **********************************************************************************************


def keywordOnlyArguments(a, b, *, c, d):
	"""
		*后面必须指定关键字参数.

		Args:
			a.
			b.
			c.
			d.

		Returns:
			.

		Examples:
	"""
	print(a, b, c, d)


if __name__ == '__main__':
	# 会报错TypeError: keywordOnlyArguments() takes 2 positional arguments but 4 were given
	# keywordOnlyArguments(1, 2, 3, 4)
	keywordOnlyArguments(1, 2, c=3, d=4)
