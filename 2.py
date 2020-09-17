'''
Second day of 30 day challenge
Hash Tables: Ransom Note (Hacker Rank)
'''
from collections import Counter
'''
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
'''
def checkMagazine(magazine, note):
    return "Yes" if (Counter(magazine) & Counter(note)) == Counter(note) else "No"

def main():
    mn = input().split()       #take the integer values from the user

    m = int(mn[0])
    n = int(mn[1])

    magazine = input().rstrip().split() #the magazine from which the note will be cut
    note = input().rstrip().split() #the note which has to be cut

    result = checkMagazine(magazine, note)
    print(result)

if __name__ == '__main__':
    main()
