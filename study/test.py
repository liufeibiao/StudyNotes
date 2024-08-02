import torch

# 创建张量
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])

# 张量运算
z = x + y
print(z)

# 自动求导
x = torch.ones(2, 2, requires_grad=True)
y = x + 2
z = y * y * 3
out = z.mean()

out.backward()  # 自动求导
print(x.grad)   # 查看梯度
