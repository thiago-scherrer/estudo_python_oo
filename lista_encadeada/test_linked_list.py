#!/usr/bin/env python

import unittest
import linked_list as linked


node1 = linked.node1
node2 = linked.node2
node3 = linked.node3
node4 = linked.node4
print_list = linked.PrintResult.linked_list(node1)
mock_list = ["node1", "node2", "node3", "node4"]


class TestNode(unittest.TestCase):
    def teste_node1(self):
        self.assertEqual(node1.value, "node1")

    def teste_node2(self):
        self.assertEqual(node2.value, "node2")

    def teste_node3(self):
        self.assertEqual(node3.value, "node3")

    def teste_node4(self):
        self.assertEqual(node4.value, "node4")

    def teste_main(self):
        self.assertEqual(print_list, mock_list)


if __name__ == '__main__':
    unittest.main()
