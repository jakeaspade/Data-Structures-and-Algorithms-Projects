"""
Project 1
CSE 331 FS24 (Onsay)
Authors of DLL: Andrew McDonald, Alex Woodring, Andrew Haas, Matt Kight, Lukas Richters, 
                Anna De Biasi, Tanawan Premsri, Hank Murdock, & Sai Ramesh
Authors of Application: Leo Specht
starter.py
"""

from __future__ import annotations

from contextlib import nullcontext
from typing import TypeVar, List, Tuple, Optional

from Scripts.activate_this import prev_length

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)
DLL = TypeVar("DLL")

# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    DO NOT MODIFY
    """
    __slots__ = ["value", "next", "prev", "children_branch"]

    def __init__(self, value: T, next: Node = None, prev: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        DO NOT MODIFY
        """
        self.next = next
        self.prev = prev
        self.value = value

        # Variable only used in application problem.
        self.children_branch: Optional[GitBranch] = None

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        DO NOT MODIFY
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        DO NOT MODIFY
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        DO NOT MODIFY
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        DO NOT MODIFY
        """
        return repr(self)

    # MODIFY BELOW #
    # Refer to the classes provided to understand the problems better #

    def empty(self) -> bool:
        """
        Return boolean indicating whether DLL is empty.

        :return: True if DLL is empty, else False.
        """
        if self.head is None:
            return True
        else:
            return False


    def push(self, val: T, back: bool = True) -> None:
        """
        Create Node containing `val` and add to back (or front) of DLL. Increment size by one.

        :param val: value to be added to the DLL.
        :param back: if True, add Node containing value to back (tail-end) of DLL;
            if False, add to front (head-end).
        :return: None.
        """
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
            self.size += 1
        elif back:
            self.tail.next = Node(val)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.size += 1
        elif not back:
            self.head.prev = Node(val)
            self.head.prev.next = self.head
            self.head = self.head.prev
            self.size += 1


    def pop(self, back: bool = True) -> None:
        """
        Remove Node from back (or front) of DLL. Decrement size by 1. If DLL is empty, do nothing.

        :param back: if True, remove Node from (tail-end) of DLL;
            if False, remove from front (head-end).
        :return: None.
        """
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            elif back:
                self.tail.prev.next = self.tail.next
                self.tail = self.tail.prev
            elif not back:
                self.head.next.prev = self.head.prev
                self.head = self.head.next
            self.size -= 1


    def list_to_dll(self, source: List[T]) -> None:
        """
        Construct DLL from a standard Python list.

        :param source: standard Python list from which to construct DLL.
        :return: None.
        """
        self.head = None
        self.tail = None
        self.size = 0
        for elem in source:
            self.push(val=elem)


    def dll_to_list(self) -> List[T]:
        """
        Construct standard Python list from DLL.

        :return: standard Python list containing values stored in DLL.
        """
        current_node = self.head
        dll_list = []
        while current_node != None:
            dll_list.append(current_node.value)
            current_node = current_node.next
        return dll_list

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Construct list of Nodes with value val in the DLL and return the associated Node list

        :param val: The value to be found
        :param find_first: If True, only return the first occurrence of val. If False, return all
        occurrences of val
        :return: A list of all the Nodes with value val.
        """
        current_node = self.head
        found = []
        while current_node != None:
            if current_node.value == val:
                found.append(current_node)
                if find_first:
                    break
            current_node = current_node.next
        return found

    def find(self, val: T) -> Node:
        """
        Find first instance of `val` in the DLL and return associated Node object..

        :param val: value to be found in DLL.
        :return: first Node object in DLL containing `val`.
            If `val` does not exist in DLL, return None.
        """
        node = self._find_nodes(val=val, find_first=True)
        if node == []:
            return None
        else:
            return node[0]

    def find_all(self, val: T) -> List[Node]:
        """
        Find all instances of `val` in DLL and return Node objects in standard Python list.

        :param val: value to be searched for in DLL.
        :return: Python list of all Node objects in DLL containing `val`.
            If `val` does not exist in DLL, return empty list.
        """
        nodes = self._find_nodes(val=val, find_first=False)
        if nodes == []:
            return []
        else:
            return nodes

    def _remove_node(self, to_remove: Node) -> None:
        """
        Given a node in the linked list, remove it.
        Should only be called from within the DLL class.

        :param to_remove: node to be removed from the list
        :return: None
        """
        if to_remove == self.tail:
            self.pop()
        elif to_remove == self.head:
            self.pop(back=False)
        else:
            to_remove.prev.next = to_remove.next
            to_remove.next.prev = to_remove.prev
            self.size -= 1


    def remove(self, val: T) -> bool:
        """
        Delete first instance of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: True if Node containing `val` was deleted from DLL; else, False.
        """
        current_node = self.head
        removed = False
        while current_node != None and not removed:
            if current_node.value == val:
                self._remove_node(current_node)
                removed = True
            current_node = current_node.next
        return removed

    def remove_all(self, val: T) -> int:
        """
        Delete all instances of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: integer indicating the number of Nodes containing `val` deleted from DLL;
                 if no Node containing `val` exists in DLL, return 0.
        """
        current_node = self.head
        removed = 0
        while current_node != None:
            if current_node.value == val:
                self._remove_node(current_node)
                removed += 1
            current_node = current_node.next
        return removed

    def reverse(self) -> None:
        """
        Reverse DLL in-place by modifying all `next` and `prev` references of Nodes in the
        DLL and resetting the `head` and `tail` references.

        :return: None.
        """
        current_node = self.head
        while current_node != None:
            temp = current_node.prev
            current_node.prev = current_node.next
            current_node.next = temp
            if current_node == self.head:
                new_tail = current_node
            if current_node == self.tail:
                new_head = current_node
            current_node = current_node.prev
        if self.head is not None and self.tail is not None:
            self.head = new_head
            self.tail = new_tail


# MODIFY BELOW #
# Refer to specs to know what can be changed #
class GitBranch(DLL):
    def __init__(self, name: str = "main", parent_node: Node = None):
        self.name = name
        self.parent_node = parent_node
        super().__init__()

    def push_commit(self, value: T) -> Optional[Node]:
        """
        Push a value in the Git timeline.
        If the value is the first in the branch, assign previous node to be the parent node.
        :param value: Value to be added to the branch.
        :return: The new last node of the branch.
        """
        pass

    def get_first_commit(self) -> Node:
        """
        Get first commit on the branch/timeline.
        :return: The first commit node on the branch.
        """
        pass
    
    def get_last_commit(self) -> Node:
        """
        Get the last commit on the branch/timeline.
        :return: The last commit node on the branch.
        """
        pass


class Git:
    __slots__ = ["current_branch", "start", "selected_commit", "visited_branches"]
    
    def __init__(self):
        # Reference to the original/main branch.
        self.start = GitBranch()
        # Current working branch.
        self.current_branch = self.start
        # The currently selected commit of a branch, which might not be in the active working branch or the main branch,
        # as we may be moving backwards or forward in the commit history
        self.selected_commit: Node = None
        # Keeps track of branches that have been visited on backwards movements.
        self.visited_branches = set()

    def get_current_commit(self) -> Optional[str]:
        """
        Return the value stored in the currently selected commit.
        :return: current working commit of tree.
        """
        pass

    def get_current_branch_name(self) -> Optional[str]:
        """
        Return the name of the current working/active branch.
        :return: Name of current working branch.
        """
        pass

    def commit(self, message: str) -> None:
        """
        Commit to the timeline if it is the last element in the commit.
        If current working commit is not the last commit, raise exception.
        :param message: Message to be added to commit.
        """
        pass

    def backwards(self) -> None:
        """
        Moves the reference of the current working commit back one commit.
        If already in the first commit of tree, do not move.
        """
        pass

    def forward(self) -> None:
        """
        Move the reference of the current working commit forward one commit.
        Keep the working commit on the working branch if multiple branches available.
        If already in the last commit of tree, do not move.
        """
        pass

    # DO NOT MODIFY BELOW #
    # The following methods are already implemented for you to (1) better understand how Git works,
    # (2) better understand tests.py as they are called in tests.py.
    def checkout_commit(self, message) -> None:
        """
        Check out any commit in the tree, moving the current selected branch to that commit's branch.
        If the commit is found, change the current selected branch to be the parent branch of the commit.
        If no such commit exists, raise an exception.

        :param message: Commit message to look for.
        """
        existing_commit = self.find_commit(self.start, message)
        if existing_commit is not None:
            self.current_branch = existing_commit[0]
            self.selected_commit = existing_commit[1]
            return

        raise Exception("Commit is not existent")

    def checkout_branch(self, name) -> None:
        """
        Check out a tree branch, and move the working commit to the last commit on the branch.
        If the branch with the given name already exist, change the current branch to be that one, and change the current
        commit to be the last commit on the branch. If branch does not exist and current working commit does not have a
        branch, then create a branch from that commit.

        :param name: The branch name to look for.
        :return: None.
        """
        existing_branch = self.find_branch(self.start, name)

        # Branch exists
        if existing_branch is not None:
            self.current_branch = existing_branch
            self.selected_commit = existing_branch.get_last_commit()
            self.visited_branches.clear()
            return

        # Trying to create a branch on an empty head (No commits on branch yet)
        if self.selected_commit is None:
            raise Exception("Branches cannot be created on empty commits")

        if self.selected_commit.children_branch is None:
            self.selected_commit.children_branch = GitBranch(name, self.selected_commit)
            self.current_branch = self.selected_commit.children_branch
            self.selected_commit = self.selected_commit.children_branch.head
            self.visited_branches.clear()

        else:
            raise Exception("Can't create multiple branches based of same commit")

    def find_branch(self, start: GitBranch, name: str) -> GitBranch | None:
        """
        Iteratively find branch on the tree.

        :param start: Current tree to look for in.
        :param name: Name of branch to look for.
        :return: Branch reference if found, else None.
        """
        next_trees = [start]
        while next_trees:
            start = next_trees.pop()
            if start.name == name:
                return start
            node = start.get_first_commit()
            while node:
                if node.children_branch:
                    next_trees.append(node.children_branch)
                node = node.next
        return

    def find_commit(self, start: GitBranch, message: str) -> Tuple[GitBranch, Node] | None:
        """
        Iteratively find a commit based on the given commit message.

        :param start: Current branch to look for commit
        :param message: Commit message to look for
        :return: If found commit, return branch and commit node, else None
        """
        next_trees = [start]
        while next_trees:
            start = next_trees.pop()
            node = start.get_first_commit()
            while node:
                if node.value == message:
                    return start, node
                if node.children_branch:
                    next_trees.append(node.children_branch)
                node = node.next
        return
