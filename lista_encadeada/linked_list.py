#!/usr/bin/env python
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.start = None

    def insertNode(self, value):
        n = Node(value)

        if(self.start):
            n2 = self.start
            while(n2.next):
                n2 = n2.next
            n2.next = n
        else:
            self.start = n
        return n.value

    def showList(self):
        n2 = self.start
        result = []
        while(n2):
            print(n2.value)
            result.append(n2.value)
            n2 = n2.next
        return result

    def removeNode(self, node):
        n2 = self.start
        result = []

        while(n2):
            if str(n2.next) == node:
                f = n2
                s = n2.next
                f.next = s.next
            if str(n2) == node:
                f = n2
                s = n2.next
                f.next = s.next
                n2.value = s

            result.append(n2.value)
            n2 = n2.next

        return result


def main():
    linked = LinkedList()
    linked.insertNode("node1")
    linked.insertNode("node2")
    linked.insertNode("node3")
    linked.insertNode("node4")
    linked.insertNode("node5")
    linked.removeNode("node2")
    linked.showList()


if __name__ == "__main__":
    main()
