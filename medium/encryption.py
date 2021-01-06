# https://www.hackerrank.com/challenges/encryption/problem

def encryption(s):
    n = len(s)
    r, c = math.floor(math.sqrt(n)), math.ceil(math.sqrt(n))
    if r*c<n:
        r+=1
    
    res =[]
    for i in range(c):
        temp = []
        j = 0
        while i+j<n:
            temp.append(s[i+j])
            j+=c
        res.append(''.join(temp))
        
    print(' '.join(res))
        