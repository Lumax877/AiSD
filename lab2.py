from typing import Any

class Node:
    def __init__(self, value: Any = None):
        self.value: Any = value
        self.next: "Node" = None

class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None #?

    def push(self, value: Any) -> None:
        elem = Node(value)
        elem.next = self.head
        self.head = elem

    def append(self, value: Any) -> None:
        elem = Node(value)
        if self.head == None:
            self.head = elem
            return
        last = self.head
        while (last.next != None):
            last = last.next
        last.next = elem

    def node(self, at: int) -> None:
        point = self.head
        num = 0
        while point != None:
            if num == at:
                return point
            num = num + 1
            point = point.next

    def insert(self, value: Any, after: Node) -> None:
        elem = Node(value)
        if after.next != None:
            temp = after.next
            after.next = elem
            elem.next = temp

    def pop(self) -> Any:
        rmv = self.head
        self.head = self.head.next
        return rmv.value

    def remove_last(self) -> Any:
        if(self.head != None):
            if(self.head.next == None):
                self.head = None
            else:
                temp = self.head
                while(temp.next.next != None):
                    temp = temp.next
                last = temp.next
                val = last
                temp.next = None
                last = None
                return val.value

    def remove(self, after: Node) -> Any:
        if after.next == None:
            return
        if after.next.next != None:
            after.next = after.next.next
        else:
            after.next = None
            self.tail = after

    def len(self):
        if self.head != None:
            current = self.head
            counter = 1
            while current.next != None:
                counter += 1
                current = current.next
            return counter
        else:
            return 0


    def print(self):
        elem = self.head
        list = []
        while elem != None:
            list.append(elem.value)
            elem = elem.next
        list = map(str, list)
        print(" -> ".join(list))

    def __str__(self):
        elem = self.head
        list = []
        while elem != None:
            list.append(elem.value)
            elem = elem.next
        list = map(str, list)
        return " -> ".join(list)




list_ = LinkedList()

assert list_.head == None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

list_.print()


class Stack():

    def __init__(self):
        self._storage: LinkedList = LinkedList() # : Any ? || puste?

    def push(self, element: Any) -> None:
        self._storage.push(element)

    def pop(self) -> Any:
        return self._storage.pop()

    def print(self):
        if self._storage.head != None:
            point = self._storage.head
            while point != None:
                print(point.value)
                point = point.next


    def __len__(self) -> int:
        return self._storage.len()

stack = Stack()

assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2

# stack.print()

class Queue:
    def __init__(self):
        self._storage: LinkedList = LinkedList()

    def peek(self) -> Any:
        return print(self._storage.head.value)

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()


    def print(self):
        Node = self._storage.head
        list = []
        while Node != None:
            list.append(Node.value)
            Node = Node.next
        list = map(str, list)
        print(" <- ".join(list))

    def __len__(self):
        return self._storage.len()

    def __str__(self):
        node = self._storage.head
        nodes = []
        while node != None:
            nodes.append(node.value)
            node = node.next
        nodes = map(str, nodes)
        return ", ".join(nodes)

queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

# queue.peek()

assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2

# queue.print()









