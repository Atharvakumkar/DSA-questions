class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def showInfo(self):
        print("Node Value --> ", str(self.data))


class DataStack:
    def __init__(self):
        self.top = None

    def push(self, newNode):
        if self.top is None:
            self.top = newNode
        else:
            newNode.nextNode = self.top
            self.top = newNode

    def pop(self):
        if self.top is None:
            return None
        else:
            s = self.top.data
            self.top = self.top.nextNode
            return s

    def isEmpty(self):
        return self.top is None

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data


def braceStack():
    myStack = DataStack()
    expr = input("Enter arithmetic expression: ")

    pairs = {')': '(', '}': '{', ']': '['}

    for i in expr:
        if i in "{[(":
            node = Node(i)
            myStack.push(node)
            print("Pushed:", node.data)

        elif i in "]})":
            p = myStack.peek()
            print("Peek value:", p)

            x = myStack.pop()
            print("Popped:", x)

            if x != pairs[i]:
                return False

    return myStack.isEmpty()



if braceStack():
    print("Delimiter is balanced")
else:
    print("Imbalanced")

braceStack()
