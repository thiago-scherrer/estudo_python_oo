#!/usr/bin/env python

import unittest
import linked_list


lk = linked_list.LinkedList()
mock1 = ["node_example1", "node_example2"]


class TestAddNode(unittest.TestCase):

    def test_add_node1(self):
        want = "node_example1"
        got = lk.insertNode("node_example1")
        self.assertEqual(want, got)

    def test_add_node2(self):
        want = "node_example2"
        got = lk.insertNode("node_example2")
        self.assertEqual(want, got)


class TestPrint(unittest.TestCase):

    def test_print_list(self):
        want = mock1
        got = lk.showList()
        self.assertEqual(want, got)


class TestRemove(unittest.TestCase):

    def test_remove_node(self):
        want = mock1
        got = lk.removeNode("node_example3")
        self.assertEqual(want, got)


class TestSearch(unittest.TestCase):

    def test_search(self):
        want = ["node_example2"]
        got = lk.searchList("node_example2")
        self.assertEqual(want, got)


if __name__ == '__main__':
    unittest.main()
