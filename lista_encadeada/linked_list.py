#!/usr/bin/env python
import os


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")
node4 = Node("node4")
node1.next = node2
node2.next = node3
node3.next = node4


class PrintResult:
    def linked_list(node):
        result = []
        while node:
            result.append(node.value)

            if os.getenv("DEBUG") == "True":
                print(result)

            node = node.next

        return result


def main():
    PrintResult.linked_list(node1)


if __name__ == "__main__":
    main()
