def separate(p):
	cnt = 1
	start = p[0]
	u = '' + p[0]
	v = ''
	for i in range(1,len(p)):
		if p[i] != start:
			cnt -= 1
		else:
			cnt += 1
		if cnt == 0:
			break
	u = p[:i+1]
	v = p[i+1:]
	return u,v
def true_p(p):
	n1 = 0
	n2 = 0
	for i in p:
		if n1 < n2:
			return False
		if i == '(':
			n1 += 1
		else:
			n2 += 1
	return True

def reverse_s(p):
	temp = ''
	for i in p:
		if i == '(':
			temp += ')'
		else:
			temp += '('
	return temp

def solution(p):
	if true_p(p) or not p:
		return p
	else:
		u, v = separate(p)
		if not true_p(u):
			temp = '(' + solution(v) + ')'
			temp2 = reverse_s(u[1:len(u)-1])
			return temp + temp2
		else:
			return u + solution(v)
			
# 프로그래머스 풀이
def solution2(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))

if __name__ == '__main__':
	p = ["(()())()",")(","()))((()"]
	for i in p:
		print(solution(i))