'''
Fifth day
Longest Common Preifx - Leetcode
'''
def commonPrefix(lst):
    if len(lst) == 0:
        return ""

    prefix = []
    first_word = lst[0]
    for i in range(len(first_word)):
        curr_char = first_word[i]
        for j in range(1, len(lst)):
            curr_word = lst[j]
            if len(curr_word) < i+1 or curr_word[i] != curr_char:
                return ''.join(prefix)

        prefix.append(curr_char)
    return ''.join(prefix)

if __name__ == '__main__':

    lst = [item for item in input().split()]
    #print(lst)
    res = commonPrefix(lst)
    print(res)
