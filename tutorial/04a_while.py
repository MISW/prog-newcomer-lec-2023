# while文のサンプル

n = int(input("2以上の整数を入力してください: "))

# https://en.wikipedia.org/wiki/Collatz_conjecture
while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n)
    
    