S = int(input())
cnt = 0
for i in range(1,S):
	if S < i:
		break
	S -= i
	cnt += 1

print(cnt)
