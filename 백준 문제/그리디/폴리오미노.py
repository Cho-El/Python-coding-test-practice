pol = [('XXXX','AAAA'),('XX','BB')]
s = input()
for n, word in enumerate(pol):
	s = s.replace(word[0], word[1])

if 'X' in s:
	print('-1')
else:
	print(s)