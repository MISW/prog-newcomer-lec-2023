# 二次元配列のサンプル
import copy

# 0で初期化された長さ4の1次元配列
zeroes_arr = [0] * 4
# 0で初期化された4x4の2次元配列
zeroes_mat = [copy.copy(zeroes_arr) for _ in range(4)]
# 0で初期化された4x4x4の3次元配列
zeroes_tensor = [copy.deepcopy(zeroes_mat) for _ in range(4)]

print(zeroes_tensor)

print(zeroes_tensor[0][0][0])
print(zeroes_tensor[1][0][0])

zeroes_tensor[1][0][0] = 1

print(zeroes_tensor)
