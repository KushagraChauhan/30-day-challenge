'''
Third day
Remove Duplicates from sorted Array - Leetcode
'''

def removeDuplicates(arr):
    arr_final = list(set(arr))
    #print(arr_final)
    return len(arr_final)


def main():
    arr = [int(x) for x in input().split()]
    #print(arr)
    res = removeDuplicates(arr)
    print(res)

if __name__ == '__main__':
    main()
