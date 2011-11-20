import sys

def is_valid(card_no):
  luhn_sum = _get_luhn_sum(card_no)
  length_of_card = len(card_no)
  return (length_of_card == 14 or length_of_card == 16) and luhn_sum % 10 == 0

def _get_luhn_sum(card_no):
  index=0
  sum=0
  alternate_digits = card_no[-2::-2]
  other_digits = card_no[-1::-2]

  return _sum(alternate_digits) + _sum(other_digits, multiplier=1)

def _sum(num_as_string, multiplier=2):
    sum = 0
    for num in num_as_string:
        sum = sum + _sum_of_digits(multiplier * int(num))

    return sum

def _sum_of_digits(num):
  sum = 0
  for c in str(num):
    sum = sum + int(c)

  if sum > 9:
    return _sum_of_digits(sum)

  return sum
     
if __name__ == "__main__":
  card_no = sys.argv[1]
  print "original number %s" % card_no
  print is_valid(card_no)
