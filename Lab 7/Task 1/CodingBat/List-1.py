def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  return False

def same_first_last(nums):
  if len(nums)==1:
    return True
  if len(nums)==0:
    return False
  return nums[0] == nums[-1]

def make_pi():
  return[3,1,4]

def common_end(a, b):
  return a[-1] == b[-1] or a[0] == b[0]

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  l = nums[1:]
  l.append(nums[0])
  return l

def reverse3(nums):
  return list(reversed(nums))

def max_end3(nums):
  max = nums[0] if nums[0] > nums[-1] else nums[-1]
  l = [max for i in nums]
  return l

def sum2(nums):
  if len(nums)<2:
    return sum(nums)
  return nums[0] + nums[1]

def middle_way(a, b):
  return [a[1],b[1]]

def make_ends(nums):
  return [nums[0],nums[-1]]

def has23(nums):
  return 2 in nums or 3 in nums
