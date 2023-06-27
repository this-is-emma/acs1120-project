#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(n) because we must traverse the whole list and append the item at the end."""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        # TODO: Else append node after tail
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) because the number of nodes in the list does not affect the prepend operation"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Prepend node before head, if it exists
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = None
            self.head = new_node
            self.tail = new_node

    def find(self, matcher):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(1) if the element we are searching is located at the beginning of the linked list
        TODO: Worst case running time: O(n) if it's located at the end of the linked list"""
        # TODO: Loop through all nodes to find item, if present return True otherwise False
        match_found = False
        node = self.head
        while node is not None:
            if matcher == node.data:
                match_found = True
                break
            node = node.next
        return match_found

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) if the element to be deleted is located at the beginning of the linked list
        TODO: Worst case running time: O(n) if it's located at the end of the linked list"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        # current_node = None
        match_found = False
        # next_node = None
        # node = self.head
        # previous_node = node
        # while node is not None:
        #     next_node = node.next
        #     # print('Node is not empty! Currently contains: ', node.data)
        #     if item == node.data:
        #         # print(f'There is a match! item {item} matches {node.data}')
        #         match_found = True
        #         if self.head == node:
        #             previous_node = None
        #             self.head = node.next
        #             break
        #         elif self.tail == node:
        #             print(f'the node was the TAIL!')
        #             print('next node is: ',next_node)
        #             print('previous node is: ', previous_node)
        #             # previous_node.next = next_node
        #             self.tail = previous_node
        #             self.tail.next = None
        #             print('ll tail is now: ', self.tail)
        #             break
        #         else:
        #             # print(f'the node WASNT the head - unlinking current node {node.data}, taking previous node {previous_node.next.data} to point towards {node.next.data}')
        #             previous_node.next = next_node
        #             print('self is now: ', self)
        #             print("tail is: ",self.tail.data)
        #             break

        #     previous_node = node
        #     node = node.next
        # if match_found == False:
        #     raise ValueError('Item not found: {}'.format(item))
        if self.head is None:
            raise ValueError('Item not found: {}'.format(item))

        # If the key to be deleted is in the head node
        if self.head.data == item:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current is not None and current.data != item:
            prev = current
            current = current.next

        if current is None:
            raise ValueError('Item not found: {}'.format(item))

        # If the key to be deleted is in the last node
        if current == self.tail:
            self.tail = prev

        prev.next = current.next


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
