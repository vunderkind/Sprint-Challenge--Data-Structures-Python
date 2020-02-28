from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def __str__(self):
        return str(self.storage)

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            last_accessed = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if last_accessed == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.current

        list_buffer_contents.append(current.value)
        if current.next:
            next_item = current.next
        else:
            next_item = self.storage.head

        while next_item != current:
            list_buffer_contents.append(next_item.value)
            if next_item.next:
                next_item = next_item.next
            else:
                next_item = self.storage.head
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current_index = 0

    def append(self, item):

        self.storage[self.current_index] = item
        self.current_index += 1
        if self.current_index == self.capacity:
            self.current_index = 0

    def get(self):
        return [i for i in self.storage if i]
