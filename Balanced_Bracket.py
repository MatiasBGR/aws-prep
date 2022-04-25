

from email.mime import base
from operator import le
from re import L


sample_case_01_t1 = '{[()]}'
sample_case_01_t2 = '{[(])}'
sample_case_01_t3 = '{{[[(())]]}}'

sample_case_02_t1 = '{{([])}}'
sample_case_02_t2 = '{{)[](}}'
sample_case_02_t3 = '{{[[(())]]}}'

sample_case_03_t1 = '{(([])[])[]}'
sample_case_03_t2 = '{(([])[])[]]}'
sample_case_03_t3 = '{(([])[])[]}[]'


    
def isBalanced(s):
    if len(s) % 2 != 0: return 'NO'
    i = 0
    while True:
        if len(s) == 2: return 'YES' if  base_case(s) else 'NO'
        if inverse(s[i]) == s[i+1]:
            s = s[:i] + s[i+2:]
            i = 0
        else:
            i += 1

def inverse(s):
    if s == '(': return ')'
    if s == '[': return ']'
    if s == '{': return '}'
    return None

def valid(s):
    return s in ['(','{','[']

def base_case(s):
    if s == '()' or s == '[]' or s == '{}':
        return True
    return False

def base_case_v2(s):
    if s == '()' or s == '[]' or s == '{}':
        return ''
    return s
def isBalanced_recursive(s):
    return _isBalanced_recursive(s,0)
def _isBalanced_recursive(s, p):
    print('S_  :',s)
    print ('S_p :',s[p:])
    if p >= len(s)-1: return 'NO'
    if len(s) == 2: return 'YES' if  base_case(s) else 'NO'
    if inverse(s[p]) == s[p+1]:
        return _isBalanced_recursive(s[:p] + s[p+2:])
    if not valid(s[p+1]): return 'NO'
    else:
        return _isBalanced_recursive(s, p+1)




def test():
    print(isBalanced_recursive(sample_case_01_t1))
    print(isBalanced_recursive(sample_case_01_t2))
    # print(isBalanced_recursive(sample_case_01_t3))
    # print(isBalanced_recursive(sample_case_02_t1))
    # print(isBalanced_recursive(sample_case_02_t2))
    # print(isBalanced_recursive(sample_case_02_t3))
    # print(isBalanced_recursive(sample_case_03_t1))
    # print(isBalanced_recursive(sample_case_03_t2))
    # print(isBalanced_recursive(sample_case_03_t3))