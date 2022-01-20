# s = list(map(int, input()))

# l = [s[0]]

# for i in range(1, len(s)):
#     if s[i] != l[-1]:
#         l.append(s[i])

# zero = l.count(0)
# one = l.count(1)

# print(min(zero, one))

s = list(map(int, input()))
count0 = count1 = 0

if s[0]==0:
    count0 += 1
else:
    count1 += 1
    
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == 0:
            count0 += 1
        else:
            count1 += 1

print(min(count1, count0))
            
