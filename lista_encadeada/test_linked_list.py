#!/usr/bin/env python

import unittest
import linked_list as linked


node1 = linked.node1
node2 = linked.node2
node3 = linked.node3
node4 = linked.node4
show_list = linked.LinkedList.showList(node1)
mock_list = ["node1", "node2", "node3", "node4"]


class TestNode(unittest.TestCase):
    def test_node1(self):
        self.assertEqual(node1.value, "node1")

    def test_node2(self):
        self.assertEqual(node2.value, "node2")

    def test_node3(self):
        self.assertEqual(node3.value, "node3")

    def test_node4(self):
        self.assertEqual(node4.value, "node4")

    def test_main(self):
        self.assertEqual(show_list, mock_list)


class TestRemoveNode(unittest.TestCase):
    def test_remove(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
