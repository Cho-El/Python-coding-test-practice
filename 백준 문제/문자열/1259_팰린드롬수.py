while True:
	n = int(input())
	check = 1

	if n == 0:
		break

	sn = str(n)
	len_s = len(sn)

	for i in range((len(sn)+1)//2):
		if sn[i] != sn[len(sn)-1-i]:
			check = 0
			break
	if check:
		print('yes')
	else:
		print('no')
