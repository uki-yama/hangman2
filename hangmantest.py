import random

def hangman():
    words = ["dog", "cat", "bird"]
    word = words[random.randint(0, 2)]
    wrong = 0
    stages = ["",\
              "_____     ",\
              "|         ",\
              "|    |    ",\
              "|    o    ",\
              "|   /|    ",\
              "|   /     ",\
              "|         ",\
              ]
    win = False
    rletters = list(word)
    board = ["_"]*len(word)
    print("ハングマンへようこそ")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "一文字入力してください"
        answer = input(msg)
        if answer in rletters:
            num = rletters.index(answer)
            board[num] = answer
            rletters[num] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print(board)
            win = True
            break
    if not win:
        print("\n".join(stages[0:e]))
        print("あなたの負け。正解は{}".format(word))
    


    
