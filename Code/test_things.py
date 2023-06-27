from dictogram import Dictogram
from listogram import Listogram
from linkedlist import LinkedList

ll = LinkedList(['A', 'B', 'C', 'D', 'E'])


print('delete A!')
print(ll.delete('A'))
print('linked list is now', ll)
print('delete E!')
print(ll.delete('E'))
print('linked list is now', ll)
print('delete C!')
print(ll.delete('C'))
print('linked list is now', ll)
print('delete D!')
print(ll.delete('D'))
print('linked list is now', ll)
print('delete B!')
print(ll.delete('B'))
print('linked list is now', ll.tail)
