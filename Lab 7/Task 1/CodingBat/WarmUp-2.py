def string_times(str, n):
  return str * n

def front_times(str, n):
  return str[:3] * n

def string_bits(str):
  s = ''
  for i in range(0,len(str)):
    if i%2==0:
      s+=str[i]
  return s

def string_splosion(str):
  s = ''
  for i in range(0,len(str)):
    s+=str[:i+1]
  return s

def last2(str):
  if len(str) < 2:
    return 0
  cnt = 0
  s = str[-2] + str[-1]
  for i in range(0,len(str)-2):
    if str[i:i+2] == s:
      cnt+=1
  return cnt

def array_count9(nums):
  cnt = 0
  for i in nums:
    if i == 9:
      cnt+=1
  return cnt

def array_front9(nums):
  for i in nums[:4]:
    if i == 9:
      return True
  return False

def array123(nums):
  for i in range(0,len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False

def string_match(a, b):
  min = ''
  max = ''
  if len(a) > len(b):
    min = b
    max = a
  else:
    min = a
    max = b
  cnt =0
  for i in range(0,len(min)-1):
    if min[i:i+2] == max[i:i+2]:
      cnt+=1
  return cnt
