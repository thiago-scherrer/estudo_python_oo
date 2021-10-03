#!/usr/bin/env python
import linked_list


def main():
    linked = linked_list.LinkedList()

    linked.insert_node("node1")
    linked.insert_node("node2")
    linked.insert_node("node3")
    linked.insert_node("node4")
    print(linked.search("node2"))
    linked.insert_node("node5")
    linked.remove_node("node2")
    print(linked)


if __name__ == "__main__":
    main()
