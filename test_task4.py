# Test for Task 4
# @author tkgroot
#
import task4 as pd


def test_palindrome():
    res = {'valid': True, 'invalid': False}

    assert pd.palindrome(1001) == res['valid']
    assert pd.palindrome(1010) == res['invalid']
    assert pd.palindrome(8998) == res['valid']

    assert pd.palindrome(11111) == res['valid']
    assert pd.palindrome(12221) == res['valid']
    assert pd.palindrome(87694) == res['invalid']


def test_largest_palindrome():
    assert pd.main(2) == 9009
