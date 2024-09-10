class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self):
        self.head = None

    def __str__(self):
        if(self.isEmpty()):
            return "Stack is empty"
        l = []
        temp = self.head
        while(temp):
            l.append(str(temp.value))
            temp = temp.next
        return "\n".join(l)

    def isEmpty(self):
        if(self.head):
            return False
        else:
            return True

    def push(self, value):
        newNode = Node(value)
        if(self.isEmpty()):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def peek(self):
        if(self.isEmpty()):
            return None
        else:
            return self.head.value

    def pop(self):
        if(self.isEmpty()):
            return None
        else:
            temp = self.head
            value = temp.value

            self.head = self.head.next
            del temp
            return value


stack = Stack()
stack.push(0)
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack)