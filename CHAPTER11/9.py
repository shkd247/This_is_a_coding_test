def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        length = 0 
        comp = ''
        cnt = 1
        for j in range(0, len(s), i):
            temp = s[j:j+i]
            if comp == temp:
                cnt += 1
            else:
                length += len(temp)
                print('comp=',comp,'cnt=',cnt)
                if cnt != 1:
                    length += (len(str(cnt)))
                    cnt = 1
                comp = temp
        if cnt != 1:
            print('comp=',comp,'cnt=',cnt)
            length += len(str(cnt))
            
        answer = min(answer, length)
        print()
    return answer

print(solution("aabbaccc"))