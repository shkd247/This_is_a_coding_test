def mysolution():
    column = ['a','b','c','d','e','f','g','h']

    y, x = list(input())
    y = column.index(y)+1
    x = int(x)
    count = 0 

    moveX = [1, -1, 1, -1, 2, 2, -2, -2]
    moveY = [2, 2, -2, -2, 1, -1 , 1, -1]

    for i in range(8):
        if 0<x+moveX[i]<=8 and 0<y+moveY[i]<=8:   
                count+=1

    print(count)

def solution():
    input_data = input()
    row = int(input_data[1])
    column = int(ord(input_data[0])) - int(ord('a')) + 1

    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]

        if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
            result+=1

    print(result)


    