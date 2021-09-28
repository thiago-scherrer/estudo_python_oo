#!/usr/bin/env python
import node


class LinkedList:
    def __init__(self):
        self.start = None

    def inser_node(self, value):
        new_node = node.Node(value)

        if(self.start):
            n2 = self.start
            while(n2.next):
                n2 = n2.next
            n2.next = n
        else:
            self.start = n
        return n.value

    def show_list(self):
        n2 = self.start
        result = []
        while(n2):
            print(n2.value)
            result.append(n2.value)
            n2 = n2.next
        return result

    def remove_node(self, node):
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

    def search_list(self, node):
        n2 = self.start
        result = []
        while(n2):
            if node == str(n2):
                print("Search =>", n2.value)
                result.append(n2.value)
                break
            n2 = n2.next
        return result


def main():
    linked = LinkedList()
    linked.inser_node("node1")
    linked.inser_node("node2")
    linked.inser_node("node3")
    linked.inser_node("node4")
    linked.search_list("node2")
    linked.inser_node("node5")
    linked.remove_node("node2")
    linked.show_list()


if __name__ == "__main__":
    main()
