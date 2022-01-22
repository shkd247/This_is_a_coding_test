# n = list(map(int, input()))
# mid = len(n)//2
# left = n[:mid]
# right = n[mid:]
# if sum(left)==sum(right):
#     print("LUCKY")
# else:
#     print("READY")

n = input()
mid = len(n)//2
summary = 0

for i in range(mid):
    summary += n[i]
for i in range(mid, len(n)):
    summary -= n[i]

if summary == 0: 
    print("LUCKY")
else:
    print("READY")
