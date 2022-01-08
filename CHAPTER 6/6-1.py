
def mysolution():                                                                                      
    n = int(input())
    nums = [input().strip() for _ in range(n)]
    nums.sort(reverse=True)
    print(' '.join(nums))

def solution():
    n = int(input())
    nums = [input().strip() for _ in range(n)]
    
    def quick(start, end):
        if start>=end:
            return
        
        pivot = start
        left = start + 1 
        right = end
        
        while left<=right:
            while left<=end and nums[left]<=nums[pivot]:
                left += 1
            while right>start and nums[right]>=nums[pivot]:
                right += 1
            if left>right:
                nums[right], nums[pivot] = nums[pivot], nums[right]
            else:
                nums[right], nums[left] = nums[left], nums[right]
                
        quick(nums, start, right-1)
        quick(nums, right+1, end)
            
    quick(0, len(nums)-1)
    print(nums)
    
if __name__ == "__main__":
    mysolution()