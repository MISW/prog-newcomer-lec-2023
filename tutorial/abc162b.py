def main():
    n = int(input())
    res = 0
    
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        res += i
    
    print(res)

if __name__ == '__main__':
    main()