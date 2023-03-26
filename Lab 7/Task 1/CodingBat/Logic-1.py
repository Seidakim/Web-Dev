def cigar_party(cigars, is_weekend):
  if is_weekend and cigars>=40:
    return True
  if not is_weekend and cigars>=40 and cigars<=60:
    return True
  return False

def date_fashion(you, date):
  if you <=2 or date<=2:
    return 0
  if you>=8 or date>=8 :
    return 2
  return 1

def squirrel_play(temp, is_summer):
  if is_summer and temp >=60 and temp <=100:
    return True
  if not is_summer and temp >=60 and temp <=90:
    return True
  return False

def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed<=60:
      return 0
    if speed >60 and speed<=80:
      return 1
    if speed >80:
      return 2
  if speed<=65:
    return 0
  if speed >65 and speed<=85:
    return 1
  if speed >85:
    return 2

def sorta_sum(a, b):
  summ = sum([a,b])
  if summ>9 and summ<20:
    return 20
  return summ

def alarm_clock(day, vacation):
  weekends = [0,6]
  if not vacation:
    if day in weekends:
      return '10:00'
    else:
      return '7:00'
  if day in weekends:
    return 'off'
  return '10:00'

def love6(a, b):
  if a == 6 or b == 6 or a+b==6 or abs(a-b)==6:
    return True
  return False

def in1to10(n, outside_mode):
  if not outside_mode:
    if n > 0 and n <11:
      return True
    return False
  if n>9 or n<2:
    return True
  return False

def near_ten(num):
  if num%10 >7 or num%10<3:
    return True
  return False
