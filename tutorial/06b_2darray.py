# 二次元配列のサンプル
import copy

# 0で初期化された長さ8の1次元配列
zeroes_arr = [0] * 8
# 0で初期化された8x8の2次元配列
board = [copy.deepcopy(zeroes_arr) for _ in range(8)]
# board = [copy.copy(zeroes_arr) for _ in range(8)] # shallow copy

print(board)

# board[x][y]でx行目のy列目の要素にアクセスできる
print(board[0][0])
print(board[1][0])

board[1][0] = 1

print(board)
