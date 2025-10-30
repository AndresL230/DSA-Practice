class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, head):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insBack(self, val):
        node = Node(val)

        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next = node
        self.tail.prev = node

    def insFront(self, val):
        node = Node(val)
        
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def length(self):
        count = 0
        curr = self.head.next
        
        while curr != self.tail:
            count+=1
            curr = curr.next
        
        return count

    def removeFront(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def print(self):
        curr = self.head.next
        slfString = ''
        while curr != self.tail:
            slfString+= str(curr.val) +" -> "
            curr = curr.next
        print(slfString)


# Testing


ll = LinkedList(None)

print("Testing LinkedList Operations:")
print("=" * 40)

# Test inserting at the back
print("\n1. Testing insBack:")
ll.insBack(1)
ll.insBack(2)
ll.insBack(3)
print("After inserting 1, 2, 3 at back:")
ll.print()

# Test inserting at the front
print("\n2. Testing insFront:")
ll.insFront(0)
ll.insFront(-1)
print("After inserting 0, -1 at front:")
ll.print()

# Test length
print("\n3. Testing length:")
print(f"Current length: {ll.length()}")

# Test removing from front
print("\n4. Testing removeFront:")
ll.removeFront()
print("After removing from front:")
ll.print()
print(f"Length after removal: {ll.length()}")

# Test removing from end
print("\n5. Testing removeEnd:")
ll.removeEnd()
print("After removing from end:")
ll.print()
print(f"Length after removal: {ll.length()}")

# Test edge cases
print("\n6. Testing edge cases:")

# Empty list operations
ll2 = LinkedList(None)
print("Empty list length:", ll2.length())

# Single element
ll2.insBack(100)
print("Single element list:")
ll2.print()

# Remove single element
ll2.removeFront()
print("After removing single element:")
ll2.print()
print("Length:", ll2.length())

# Build a larger list
print("\n7. Testing larger list:")
ll3 = LinkedList(None)
for i in range(10):
    ll3.insBack(i)
print("List with 10 elements:")
ll3.print()
print(f"Length: {ll3.length()}")