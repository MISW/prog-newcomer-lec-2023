# 配列のサンプル

# 1次元配列の宣言
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# arr[i]でi番目の要素にアクセスできる
# 0番目から数えることに注意
print(arr[0])
print(arr[3])

# len関数で配列の長さを取得
print(len(arr))

# append関数で配列の末尾に要素を追加できる
print(arr)
arr.append(7)
print(arr)

# pop関数で配列の末尾の要素を取り出して、削除する
last_element = arr.pop()
print(last_element) # 7

# 配列のスライス [start:end]と書くと、start番目からend-1番目の要素を取り出すことができる（半開区間）
arr_sliced = arr[1:5]
print(arr_sliced)
