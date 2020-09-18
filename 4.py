'''
Third Day-
Rotate Array - Leetcode
'''

def rotate(arr,k):
    arr_final = arr
    arr_final = arr_final[k:] + arr_final[:k]
    return arr_final

def main():
    arr = [int(x) for x in input().split()]
    k = int(input())
    res = rotate(arr,k)
    print(res)

if __name__ == '__main__':
    main()
