
s = input()
num = 0
alph = []

for i in range(len(s)):
    if s[i].isalpha():
        alph.append(s[i])
    else:
        num+=int(s[i])
        
alph.sort()

print(''.join(alph)+str(num))
