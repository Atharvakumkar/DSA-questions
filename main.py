class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def show(self):
        print(self.data)


class QueueList:
    def __init__(self):
        self.head = None  # Fixed: was self.data
        self.tail = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.head == None:  # Fixed: was self.head == None
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def traverse(self):
        if self.head == None:  # Fixed: was self.head == None
            print("Queue is empty!")
        else:
            ptr = self.head
            while ptr != None:
                ptr.show()
                ptr = ptr.next

    def dequeue(self):
        if self.head == None:  # Added error checking
            print("Queue is empty! Cannot dequeue.")
            return None

        dequeued_data = self.head.data
        self.head = self.head.next

        # If queue becomes empty, update tail
        if self.head == None:
            self.tail = None

        return dequeued_data

    def peek(self):
        if self.head == None:  # Added error checking
            print("Queue is empty! Nothing to peek.")
            return None
        print(self.head.data)
        return self.head.data

    def is_empty(self):
        return self.head == None


# Example usage:
if __name__ == "__main__":
    queue = QueueList()

    # Test enqueue
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Queue contents:")
    queue.traverse()

    print(f"Peek: {queue.peek()}")

    print(f"Dequeued: {queue.dequeue()}")
    print("Queue after dequeue:")
    queue.traverse()

    print(f"Is empty: {queue.is_empty()}")