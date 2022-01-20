# from collections import deque

# s = deque()
# s.extend(list(map(int, input())))

# answer = 1

# while s:
#     num = s.pop()
#     if num != 0:
#         answer *= num
        
# print(answer)


from collections import deque

s = deque()
s.extend(list(map(int, input())))

result = s.pop()

while s:
    num = s.pop()
    if num != 0 and result !=0:
        result *= num
    else:
        result += num
        
print(result)
    



