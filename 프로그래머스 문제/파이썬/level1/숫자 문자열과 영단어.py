def solution(s): 
	#1 인덱스 번호에 해당하는 영단어 리스트 
	wordList = enumerate(["zero","one","two","three","four","five","six","seven","eight","nine"]) 
    
    #2 영단어로 표시된 문자열이 있다면 숫자(인덱스 번호)로 교체 
	for num, word in wordList :
		s = s.replace(word, str(num))
    
	#3 정수형으로 return 
	answer = int(s)
	return answer