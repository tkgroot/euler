#
#
#
prime = {}


def factor(num):
  factorArray = []
  for x in range(3,num):
    if x%1000000 == 0: print('{} done.'.format(x))
    if num%x == 0 and isPrime(x):
      factorArray.append(x)
  return factorArray


def max_factor(num):
  return max(factor(num))


def isPrime(num):
  try:
    if prime[num]: return prime[num]
  except:
    for x in range(2,num-1):
      if num%x == 0:
        prime[num] = False
        return False
    prime[num] = True
    return True


def main():
  print(max_factor(600851475143))


if __name__ == '__main__':
  main()
