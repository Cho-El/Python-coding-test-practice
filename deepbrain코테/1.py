def SimplePassword(strParam):
  result = True
  if not 7 <= len(strParam) <31: # 길이 체크
    result = False

  for s in strParam:
    if s.isupper():
      break
  else:
    result = False

  for i in range(0,10):
    if str(i) in strParam:
      break
  else:
    result = False
  
  symbol = ['<','>','?','/','~','`','!','@','#','$','%','^','&','*','(',')',',','.',';',"'",'"','{','}','[',']','-','+','=','\\']

  for s in strParam:
    if s in symbol:
      break
  else:
    result = False
  
  if strParam.find('password') == -1:
    result = False

  # code goes here
  return result

# keep this function call here 
print(SimplePassword(input()))