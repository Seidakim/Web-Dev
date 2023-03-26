def count_evens(nums):
  cnt = 0
  for i in nums:
    if i%2==0:
      cnt+=1
  return cnt

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  l = [list(sorted(nums))[i] for i in range(1,len(nums)-1)]
  if len(l)!=0:
    return sum(l)/len(l)

def sum13(nums):
  if len(nums) == 0: 
    return 0
  sum = 0
  for i in range(0,len(nums)):
    if nums[i] == 13 or (i>0 and nums[i-1]==13):
      continue
    sum+=nums[i]
  return sum

def sum67(nums):
  t = True
  sum = 0
  for i in nums:
    if i != 6:
      if t:
        sum+=i
    if i == 6:
      t = False
    if i == 7 and not t:
      t = True
  return sum
      
def has22(nums):
  for i in range(0,len(nums)-1):
    if nums[i] == nums[i+1] and nums[i]==2:
      return True
  return False
