def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  return False

def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  return False

def sum_double(a, b):
  if a == b :
    return (a+b) * 2
  return a+b

def diff21(n):
  if n<=21:
    return 21-n
  return (n-21)*2

def parrot_trouble(talking, hour):
  if talking and (hour<7 or hour>20):
    return True
  return False

def makes10(a, b):
  if a == 10 or b == 10 or a+b == 10:
    return True
  return False

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

def pos_neg(a, b, negative):
  if ((a > 0 and b< 0) or (a<0 and b> 0)) and not negative:
    return True
  if negative and (a<0 and b<0):
    return True
  return False
  
def not_string(str):
  if len(str)>2:
      if str[:3] == 'not':
        return str
      return 'not '+str
  return 'not '+str

def missing_char(str, n):
  return str[:n] + str[n+1:]

def front_back(str):
  if len(str) <= 1:
    return str
  return str[-1] + str[1:-1]+str[0]

def front3(str):
  return str[:3]*3
