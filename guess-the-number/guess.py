import os, sys, random
# import numpy as np

UPPER_LIMIT = 50000
PLAY_LIMIT = 14

def generate_random_number():
    return random.randint(1, UPPER_LIMIT)

def get_number_from_user():
    while True:
        try:
            guess = int(input("> "))
            return guess
        except ValueError:
            print("数字を入力してください.")

def run_game(player_name):
    target = generate_random_number()
    
    for i in range(PLAY_LIMIT):
        print("! 残り{}回解答できます".format(PLAY_LIMIT - i))
        guess = get_number_from_user()
        
        if guess > target:
            print("答えはもっと小さい数字です.")
        elif guess < target:
            print("答えはもっと大きい数字です.")
        else:
            print("正解です. {}さんの勝ちです!".format(player_name))
            return (True, i + 1)
    
    print("残念. 答えは{}でした. {}さんの負けです.".format(target, player_name))
    return (False, -1)

def main():
    print("""
---- 数当てゲーム ----

ルール:
1から{}までの間の乱数が生成されます. {}回以内に当てることができたら、あなたの勝ちです.
          """.format(UPPER_LIMIT, PLAY_LIMIT))
    
    name = input("あなたの名前を入力してください: ")
    is_success, count = run_game(name)
    
    # TODO: 結果を記録して、ランキングに反映させる

if __name__ == '__main__':
    main()