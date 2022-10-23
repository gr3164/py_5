# Задача 4*. Создайте игру в крестики-нолики.

import random


box = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
error = []

def Dash(x, k):
    x = str(x)
    result = ''
    for c in x:
        result = result + c + '\u0336'
    x = result
    return Print(x, k)

def Print(x, k): 
    print("     1 |  2  | 3")
    for i in range(0, len(box)):
        if i == k:
            box[i] = x 
        print(f'{i+1}| {box[i]}')  


Print(7,7)

while True:

# == Win_User ====================================================================================================================
    if box[0][1] == 'X' and box[1][1] == 'X' and box[2][1] == 'X':
        print("Победа")
        break
    if box[0][0] == 'X' and box[1][0] == 'X' and box[2][0] == 'X':
        print("Победа")
        break
    if box[0][2] == 'X' and box[1][2] == 'X'  and box[2][2] == 'X':
        print("Победа")
        break
    if box[0] == ['X', 'X', 'X']:
        Dash(box[0], 0) 
        print("Победа")
        break
    if box[1] == ['X', 'X', 'X']:
        Dash(box[1], 1) 
        print("Победа")
        break
    if box[2] == ['X', 'X', 'X']:
        Dash(box[2], 2) 
        print("Победа")
        break
    if box[0][0] == 'X' and box[1][1] == 'X' and box[2][2] == 'X':
        print("Победа")
        break
    if box[0][2] == 'X' and box[1][1] == 'X' and box[2][0] == 'X':
        print("Победа")
        break

# == Win_Bot ====================================================================================================================

    if box[0][1] == 'O' and box[1][1] == 'O' and box[2][1] == 'O':
        print("Поражение")
        break
    if box[0][0] == 'O' and box[1][0] == 'O' and box[2][0] == 'O':
        print("Поражение")
        break
    if box[0][2] == 'O' and box[1][2] == 'O'  and box[2][2] == 'O':
        print("Поражение")
        break
    if box[0] == ['O', 'O', 'O']:
        Dash(box[0], 0) 
        print("Поражение")
        break
    if box[1] == ['O', 'O', 'O']:
        Dash(box[1], 1) 
        print("Поражение")
        break
    if box[2] == ['O', 'O', 'O']:
        Dash(box[2], 2) 
        print("Поражение")
        break
    if box[0][0] == 'O' and box[1][1] == 'O' and box[2][2] == 'O':
        print("Поражение")
        break
    if box[0][2] == 'O' and box[1][1] == 'O' and box[2][0] == 'O':
        print("Поражение")
        break
# ======================================================================================================================  
  
    user = (int(input("По горизонтали: "))-1, int(input("По вертикали: "))-1)

    if user in error:
        print("Ошибка")
        user = (int(input("По горизонтали: "))-1, int(input("По вертикали: "))-1)
    else:
        box[user[0]][user[1]] = 'X'
        error.append((user[0], user[1]))
    
    bot = (random.randint(0,2),random.randint(0,2))
    if bot in error:
        while True:
            bot = (random.randint(0,2),random.randint(0,2))
            print(bot)
            if not bot in error:
                break
    else:       
        box[bot[0]][bot[1]] = 'O'
        error.append((bot[0], bot[1]))
    
    Print(7, 7)
   
         
        
    