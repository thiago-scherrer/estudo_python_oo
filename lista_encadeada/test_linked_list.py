#!/usr/bin/env python
import unittest
import linked_list


lk = linked_list.LinkedList()
mock1 = ["node_example1", "node_example2"]


class TestAddNode(unittest.TestCase):

    def test_add_node1(self):
        expected = "node_example1"
        got = lk.inser_node("node_example1")
        self.assertEqual(expected, got)

    def test_add_node2(self):
        expected = "node_example2"
        got = lk.inser_node("node_example2")
        self.assertEqual(expected, got)


class TestPrint(unittest.TestCase):

    def test_print_list(self):
        expected = mock1
        got = lk.show_list()
        self.assertEqual(expected, got)


class TestRemove(unittest.TestCase):

    def test_remove_node(self):
        expected = mock1
        got = lk.remove_node("node_example3")
        self.assertEqual(expected, got)


class TestSearch(unittest.TestCase):

    def test_search(self):
        expected = ["node_example2"]
        got = lk.search_list("node_example2")
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()
