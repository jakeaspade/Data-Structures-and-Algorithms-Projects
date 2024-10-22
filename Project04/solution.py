"""
CSE331 Project 4 FS24
Circular Double-Ended Queue
solution.py
"""

from typing import TypeVar, List

T = TypeVar('T')


class CircularDeque:
    """
    Representation of a Circular Deque using an underlying python list
    """

    __slots__ = ['capacity', 'size', 'queue', 'front', 'back']

    def __init__(self, data: List[T] = None, front: int = 0, capacity: int = 4):
        """
        Initializes an instance of a CircularDeque
        :param data: starting data to add to the deque, for testing purposes
        :param front: where to begin the insertions, for testing purposes
        :param capacity: number of slots in the Deque
        """
        if data is None and front != 0:
            data = ['Start']  # front will get set to 0 by a front enqueue if the initial data is empty
        elif data is None:
            data = []

        self.capacity: int = capacity
        self.size: int = len(data)
        self.queue: List[T] = [None] * capacity
        self.back: int = (self.size + front - 1) % self.capacity if data else None
        self.front: int = front if data else None

        for index, value in enumerate(data):
            self.queue[(index + front) % capacity] = value

    def __str__(self) -> str:
        """
        Provides a string representation of a CircularDeque
        'F' indicates front value
        'B' indicates back value
        :return: the instance as a string
        """
        if self.size == 0:
            return "CircularDeque <empty>"

        str_list = ["CircularDeque <"]
        for i in range(self.capacity):
            str_list.append(f"{self.queue[i]}")
            if i == self.front:
                str_list.append('(F)')
            elif i == self.back:
                str_list.append('(B)')
            if i < self.capacity - 1:
                str_list.append(',')

        str_list.append(">")
        return "".join(str_list)

    __repr__ = __str__

    #
    # Your code goes here!
    #
    def __len__(self) -> int:
        """
        INSERT DOCSTRINGS HERE!
        """
        return self.size
    def is_empty(self) -> bool:
        """
        INSERT DOCSTRINGS HERE!
        """
        if self.size == 0:
            return True
        return False

    def front_element(self) -> T:
        """
        INSERT DOCSTRINGS HERE!
        """
        if not self.is_empty():
            return self.queue[self.front]

    def back_element(self) -> T:
        """
        INSERT DOCSTRINGS HERE!
        """
        if not self.is_empty():
            return self.queue[self.back]

    def enqueue(self, value: T, front: bool = True) -> None:
        """
        INSERT DOCSTRINGS HERE!
        """
        if self.front is None and self.back is None:
            self.front = 0
            self.back = 0
        if self.size == self.capacity:
            self.grow()
        if front:
            self.queue.insert(self.front, value)
        else:
            self.queue.insert(self.back + 1, value)
        self.size += 1

    def dequeue(self, front: bool = True) -> T:
        """
        INSERT DOCSTRINGS HERE!
        """
        if not self.is_empty():
            if front:
                removed = self.queue[self.front]
                if self.front != self.back:
                    self.front = (self.front + 1) % self.capacity
                else:
                    self.front = None
                    self.back = None
            else:
                removed = self.queue[self.back]
                if self.front != self.back:
                    self.back = (self.back - 1) % 7
                else:
                    self.front = None
                    self.back = None

            self.size -= 1

            # if self.size == self.capacity / 4 and self.capacity // 2 >= 4:
            #     self.shrink()
            return removed
        return None
    def grow(self) -> None:
        """
        INSERT DOCSTRINGS HERE!
        """
        new_queue = [None] * self.capacity * 2
        j = 0
        while not self.is_empty():
            new_queue[j] = self.dequeue()
            j += 1
        self.front = 0
        self.back = j - 1
        self.size = j
        self.queue = new_queue
        self.capacity *= 2


    def shrink(self) -> None:
        """
        INSERT DOCSTRINGS HERE!
        """
        new_queue = [None] * (self.capacity // 2)
        for i in range(self.capacity // 2):
            new_queue[i] = self.queue[i]
        self.queue = new_queue
        self.capacity = self.capacity // 2

def get_winning_numbers(numbers: List[int], size: int) -> List[int]:
    """
    INSERT DOCSTRINGS HERE!
    """
    pass
    


def get_winning_probability(winning_numbers: List[int]) -> int:
    """
    INSERT DOCSTRINGS HERE!
    """
    pass


