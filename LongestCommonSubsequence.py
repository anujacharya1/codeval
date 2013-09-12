'''
Created on Jan 9, 2013

@author: anujacharya
'''
import functools
import sys

def cached(func):
  cache = {}
  def template(*args): #: template is wrapper; func is wrapped
    key = (func, )+args
    try:
      ret = cache[key]
    except KeyError:
      ret = func(*args)
      cache[key] = ret
    else:
      pass
    return ret

  functools.update_wrapper(template, func)
  return template

@cached
def LCSLength(str1, str2):
  if len(str1)==0 or len(str2)==0:
    return 0
  if str1[-1] == str2[-1]:
    return LCSLength(str1[:-1], str2[:-1])+1
  else:
    return max(LCSLength(str1, str2[:-1]), LCSLength(str1[:-1], str2))

@cached
def LCS(str1, str2):
  if len(str1)==0 or len(str2)==0:
    return ''
  if str1[-1] == str2[-1]:
    return ''.join([LCS(str1[:-1], str2[:-1]), str1[-1]])
  else:
    candidate1 = LCS(str1[:-1], str2)
    candidate2 = LCS(str1, str2[:-1])
    if len(candidate1) >= len(candidate2):
      return candidate1
    else:
      return candidate2

if __name__=='__main__':
    test_cases = open(sys.argv[1], 'r')
    result = []
    for test in test_cases:
        if ';' in test:
            data = test.split(';')
            lcs = LCS(data[0], data[1])
            print lcs
    test_cases.close()