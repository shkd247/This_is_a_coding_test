
n = int(input())
nums = list(map(int, input().split()))

nums.sort()

answer = 0 
count = 0 

for num in nums:
    count+=1
    if count >= num:
        answer += 1
        count = 0 
        
print(answer)