#!/usr/bin/env python
import node


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current_node = self.head
        result = []
        while(current_node):
            result.append(current_node.value)
            current_node = current_node.next
        return str(result)

    def current(self, value):

        if self.head is None:
            new_node = node.Node(value)
            self.head = new_node

    def insert_node(self, value):
        new_node = node.Node(value)

        try:
            current_node = self.head
            while(current_node.next):
                current_node = current_node.next
            current_node.next = new_node
        except AttributeError:
            self.current(value)

        return self

    def remove_node(self, value):
        current_node = self.head
        result = []

        while(current_node):
            if str(current_node.next) == value:
                first_node = current_node
                last_node = current_node.next
                first_node.next = last_node.next

            result.append(current_node.value)
            current_node = current_node.next

        return result

    def search(self, value):
        try:
            self.node_list().index(value)
            return value
        except ValueError:
            print("Not found")

    def node_list(self):
        current_node = self.head
        result = []

        while(current_node):
            result.append(current_node.value)
            current_node = current_node.next
        return str(result)
