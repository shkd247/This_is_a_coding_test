from collections import defaultdict

def mysolution():                                                                                      
    n = int(input())
    dict = defaultdict(int)
    for _ in range(n):
        name, score = input().split()
        dict[name] = score
        
    answer = sorted(dict.items(), key=lambda item:item[1])
    answer = [a[0] for a in answer]
    print(' '.join(answer))    

def solution():
    n = int(input())
    
if __name__ == "__main__":
    mysolution()