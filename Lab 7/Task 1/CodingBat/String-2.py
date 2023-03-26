def double_char(str):
  s =''
  for i in str:
    s+=i*2
  return s

def count_hi(str):
  cnt =0
  for i in range(0,len(str)-1):
    if str[i:i+2] == 'hi':
      cnt+=1
  return cnt

def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(0,len(str)-2):
    if str[i:i+3] == 'dog':
      dog+=1
    if str[i:i+3] == 'cat':
      cat+=1
  return cat == dog

def count_code(str):
  cnt = 0
  for i in range(0,len(str)-3):
    s = str[i:i+4]
    if s[:2] == 'co' and s[-1] =='e':
      cnt+=1
  return cnt

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  max = ''
  min = ''
  if len(a) > len(b):
    max = a
    min = b
  else:
    max = b
    min = a
  return max[len(max)-len(min):] == min

def xyz_there(str):
  if str == 'xyz':return True
  if str[:3] == 'xyz': return True
  for i in range(0,len(str)-3):
    s = str[i:i+4]
    if s[0]!='.' and s[1:]=='xyz':
      return True
  return False
