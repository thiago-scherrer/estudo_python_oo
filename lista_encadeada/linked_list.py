#!/usr/bin/env python
import node


class LinkedList:
    def __init__(self):
        self.start = None

    def __str__(self):
        current_node = self.start
        self.result = []
        while(current_node):
            self.result.append(current_node.value)
            current_node = current_node.next
        return str(self.result)

    def inser_node(self, value):
        new_node = node.Node(value)

        if(self.start):
            current_node = self.start
            while(current_node.next):
                current_node = current_node.next
            current_node.next = new_node
        else:
            self.start = new_node
        return new_node.value

    def remove_node(self, node):
        current_node = self.start
        result = []

        while(current_node):
            if str(current_node.next) == node:
                f = current_node
                s = current_node.next
                f.next = s.next
            if str(current_node) == node:
                f = current_node
                s = current_node.next
                f.next = s.next
                current_node.value = s

            result.append(current_node.value)
            current_node = current_node.next

        return result

    def search_list(self, node):
        current_node = self.start
        result = []
        while(current_node):
            if node == str(current_node):
                print("Search =>", current_node.value)
                result.append(current_node.value)
                break
            current_node = current_node.next
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
    print(linked)


if __name__ == "__main__":
    main()
