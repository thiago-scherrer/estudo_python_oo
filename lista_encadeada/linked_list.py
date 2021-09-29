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

    def insert_node(self, value):
        new_node = node.Node(value)

        if(self.start):
            current_node = self.start
            while(current_node.next):
                current_node = current_node.next
            current_node.next = new_node
        else:
            self.start = new_node
        return new_node.value

    def remove_node(self, value):
        current_node = self.start
        result = []

        while(current_node):
            if str(current_node.next) == value:
                first_node = current_node
                last_node = current_node.next
                first_node.next = last_node.next
            if str(current_node) == value:
                first_node = current_node
                last_node = current_node.next
                first_node.next = last_node.next
                current_node.value = last_node

            result.append(current_node.value)
            current_node = current_node.next

        return result

    def search_list(self, value):
        try:
            self.current_node().index(value)
            return value
        except ValueError:
            print("Not found")

    def current_node(self):
        current_node = self.start
        result = []

        while(current_node):
            result.append(current_node.value)
            current_node = current_node.next
        return str(result)


def main():
    linked = LinkedList()
    linked.insert_node("node1")
    linked.insert_node("node2")
    linked.insert_node("node3")
    linked.insert_node("node4")
    print(linked.search_list("node2"))
    linked.insert_node("node5")
    linked.remove_node("node2")
    print(linked)


if __name__ == "__main__":
    main()
