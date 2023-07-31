

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    @classmethod
    def from_str(cls, data_str):
        data_list = data_str.split(', ')
        nodes = [cls(data) for data in data_list]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.data))
            current = current.next
        return ', '.join(result)

    def delete(self, data):
        # Case 1: Empty list
        if not self:
            return None

        # Case 2: Delete the first element (head)
        if self.data == data:
            return self.next

        # Case 3: Delete an element from the middle or end
        current = self
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                break
            current = current.next
        return self

    def reverse(self):
        prev = None
        current = self
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
