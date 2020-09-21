'''
Day 6
Valid Palindrome - Leetcode
'''

def valPalindrome(s):
    if (s == s [::-1]):
        return "true"
    else:
        return "false"


if __name__ == '__main__':
    s = input()
    res = valPalindrome(s)
    print(res)
