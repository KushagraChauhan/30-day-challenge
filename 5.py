'''
Fourth Day
Valid Anagram - Leetcode
'''
from collections import Counter
def isAnagram(s,t):
    #return "True" if (sorted(s)==sorted(t)) else "False"
    return "true" if (Counter(s) == Counter(t)) else "false"

def main():
    s = input()
    t = input()

    res = isAnagram(s,t)
    print(res)

if __name__ == '__main__':
    main()
