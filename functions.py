# list to int
def n(x):
  """
  Takes in a list of numbers and return an integer.
  Example x = [1,2,3,4,5,6,7,8,9,0]
  Returns 1234567890
  params: x python list
  """
  return int(''.join(map(str, x)))
