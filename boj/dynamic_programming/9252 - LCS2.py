s1 = input()
s2 = input()

len1 = len(s1)+1
len2 = len(s2)+1

lcs = [[0]*len1 for _ in range(len2)]
result = 0

for i in range(1, len2):
    maxs = 0
    for j in range(1, len1):

        if s2[i-1] == s1[j-1]:
            maxs = lcs[i-1][j-1] + 1
            lcs[i][j] = maxs
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    result = max(result, maxs)
print(result)
if result:
    out = []
    cur = 0
    len1 -=1
    len2 -=1
    while len1 >= 1 and len2 >= 1:
        if lcs[len2][len1] == lcs[len2-1][len1]:
            len2 -= 1
        elif lcs[len2][len1] == lcs[len2][len1-1]:
            len1 -=1
        else:
            out.append(s1[len1-1])
            len1 -= 1
            len2 -= 1
    
    print(''.join(reversed(out)))