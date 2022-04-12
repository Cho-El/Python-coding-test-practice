from collections import Counter

def CountingAnagrams(strParam):
  pset = set(strParam.strip('"').split())
  result = 0
  q = list(pset)
  while q:
    now = q.pop(0)
    for i in range(len(q)):
      if Counter(q[i]) == Counter(now):
        result += 1
        q.pop(i)
    
  # code goes here
  return result

# keep this function call here 
print(CountingAnagrams(input()))