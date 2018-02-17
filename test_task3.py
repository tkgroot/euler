import task3 as pf

def test_prime():
  test = { 3:True, 4:False, 5:True, 6:False, 7:True, 8:False, 9:False, 10:False, 11:True, 12:False, 13:True, 14:False, 15:False}
  for key,val in test.items():
    assert pf.isPrime(key) == val


def test_pf():
  assert pf.factor(13195) == [5,7,13,29]

def test_max_pf():
  assert pf.max_factor(13195) == 29