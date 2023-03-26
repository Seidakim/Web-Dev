
def make_bricks(small, big, goal):
	if big * 5 == goal or small == goal:
		return True
	if big * 5 > goal:
		goal %= 5
		return goal <= small
	goal -= big * 5
	return goal <= small

def lone_sum(a, b, c):
  if a==b and b == c:
    return 0
  if a == b and b!=c:
    return c
  if a == c and c!=b:
    return b
  if b == c and a != c:
    return a
  return a+b+c
    
def lucky_sum(a, b, c):
  if a == 13:
    return 0
  if b == 13:
    return a
  if c == 13:
    return a + b
  return a + b + c

def no_teen_sum(a, b, c):
  l = [a,b,c]
  sum = 0
  for i in l:
    if i == 15 or i == 16:
      sum+=i
      continue
    if i >12 and i < 20:
      continue
    sum+=i
  return sum

def round_sum(a, b, c):
  sum = 0
  l  = [a,b,c]
  for i in l:
    mod = i%10
    if mod<5:
      sum += i-mod
    else:
      sum += i + (10-mod)
  return sum

def close_far(a, b, c):
  if abs(a-b)<=1:
    if abs(a - c)>=2 and abs(c-b)>=2:
      return True
    return False
  if abs(a-c)<=1:
    if abs(a-b)>=2 and abs(c-b)>=2:
      return True
    return False
  return False

def make_chocolate(small, big, goal):
  if  5 * big == goal:
    return 0
  if 5 * big <goal:
    if goal - 5*big <=small:
      return goal-5*big
    return -1
  if 5 * big > goal:
    x = goal//5
    if goal - 5*x <=small:
      return goal - 5*x
    return -1
