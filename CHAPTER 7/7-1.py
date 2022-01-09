
def mysolution():           
    n = int(input())
    n_nums = list(map(int, input().split()))
    
    m = int(input())
    m_nums = list(map(int, input().split()))
    
    n_nums.sort()
    m_nums.sort()
    
    n_idx = 0
    m_idx = 0 
    
    while m_idx<len(m_nums):
        while n_idx<len(n_nums) and n_nums[n_idx]<=m_nums[m_idx]:
            n_idx+=1
            
        n_idx-=1

        if n_nums[n_idx]!=m_nums[m_idx]:
            print('no', end=' ')
        else:
            print('yes', end=' ')
        
        m_idx+=1 
        
def binary(arr, target, start, end):
    if start>end:
        return None
    mid = (end+start)//2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary(arr, target, start, mid-1)
    else:
        return binary(arr, target, mid+1, end)
    
def solution():
    n = int(input())
    n_nums = list(map(int, input().split()))
    n_nums.sort()
    
    m = int(input())
    m_nums = list(map(int, input().split()))
    
    for num in m_nums:
        if binary(n_nums, num, 0, len(n_nums)):
            print('yes', end=' ')
        else:
            print('no', end=' ')
        
    
if __name__ == "__main__":
    mysolution()