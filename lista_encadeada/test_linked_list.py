#!/usr/bin/env python
import unittest
import linked_list


class TestAddNode(unittest.TestCase):
    def setUp(self):
        self.linked = linked_list.LinkedList()

    def test_add_node(self):
        expected = "node_example1"
        got = self.linked.insert_node("node_example1")
        self.assertEqual(expected, got)

    def test_print_list(self):
        self.linked.insert_node("node_example1")
        self.linked.insert_node("node_example2")
        got = self.linked
        expected = ['node_example1', 'node_example2']
        self.assertEqual(expected.__str__(), got.__str__())

    def test_remove_node(self):
        self.linked.insert_node("node_example1")
        self.linked.insert_node("node_example2")
        expected = ['node_example1', 'node_example2']
        got = self.linked.remove_node("node_example3")
        self.assertEqual(expected, got)

    def test_remove_inexistent_node(self):
        self.linked.insert_node("node_example1")
        self.linked.insert_node("node_example2")
        expected = ['node_example1', 'node_example2']
        got = self.linked.remove_node("node_example42")
        self.assertEqual(expected, got)

    def test_search(self):
        self.linked.insert_node("node_example1")
        self.linked.insert_node("node_example2")
        expected = "node_example2"
        got = self.linked.search("node_example2")
        self.assertEqual(expected, got)

    def test_node_list(self):
        self.linked.insert_node("node_example1")
        self.linked.insert_node("node_example2")
        expected = "['node_example1', 'node_example2']"
        got = self.linked.node_list()
        self.assertEqual(expected, got)

    def test_current(self):
        expected = None
        got = self.linked.current("node_example4")
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()
