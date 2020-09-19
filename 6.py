'''
Fourth Day
Reverse Linked List - Leetcode
'''

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def reverseList(self):
            curr = self.head
            while curr.next:
                temp = curr.next
                curr.next = temp.next
                temp.next = self.head
                self.head = temp

            return head

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def set_next(self, data):
        self.next = Node(data)
        return self.next



if __name__ == "__main__":

    head = Node('a')
    head.set_next('b').set_next('c').set_next('d').set_next('e')

    ll = LinkedList(head)
    ll.printList()
    ll.reverseList()
    ll.printList()
