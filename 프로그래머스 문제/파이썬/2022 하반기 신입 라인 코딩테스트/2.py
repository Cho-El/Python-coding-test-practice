from typing import List

def solution(k: int, dic: List[str], chat: str) -> str:
    answer = ''
    hash = {}
    for d in dic:
        hash[d] = 1
    chat_word = chat.split()
    for cw in chat_word:
        
    return answer

if __name__ == "__main__":
    k = [2,3]
    dic = [['slang','badword'],['abcde', 'cdefg', 'efgij']]
    chat = ['badword ab.cd bad.ord .word sl.. bad.word', '.. ab. cdefgh .gi. .z.']
    for a,b,c in zip(k, dic, chat):
        print(solution(a,b,c))