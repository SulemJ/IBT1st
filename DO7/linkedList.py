class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        if self.head is None:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        
        return False
    
    def reverse(self):
        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def has_cycle(self):
        if self.head is None:
            return False
        
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
    
    def display(self):
        items = []
        current = self.head
        while current is not None:
            items.append(str(current.data))
            current = current.next
        print(" - ".join(items) if items else "Empty list")
    
    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result


def test_linked_list():

    # Create and append
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display()  
    
    # Prepend
    ll.prepend(5)
    ll.display() 
    
    # Delete
    ll.delete(20)
    ll.display() 
    
    # Delete head
    ll.delete(5)
    ll.display()  
    
    # Delete a node that doesn't existent
    result = ll.delete(99)
    
    # Reverse
    ll.reverse()
    ll.display()  
    
    #  Check for cycle
    print(f"Has cycle? {ll.has_cycle()} ")
    
    
    # Create a list with cycle
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1  
    
    ll_cycle = LinkedList()
    ll_cycle.head = node1
    print(f"Has cycle? {ll_cycle.has_cycle()} ")
    


if __name__ == "__main__":
    test_linked_list()