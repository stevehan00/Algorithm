num = int(input())
result = 1
cnt = 0

for i in range(1, num+1):
    result = result*i

result = list(str(result))
result.reverse()

for i in result:
    if int(i) == 0:
        cnt +=1
    else:
        break

print(cnt)

