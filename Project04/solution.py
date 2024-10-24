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
        Returns the size of the deque

        :return: the size of the deque
        """
        return self.size
    def is_empty(self) -> bool:
        """
        Returns True if the deque is empty, False otherwise

        :return: True if the deque is empty, False otherwise
        """
        if self.size == 0:
            return True
        return False

    def front_element(self) -> T:
        """
        Returns the element that self.front is indexing

        :return: The front element of the deque
        """
        if not self.is_empty():
            return self.queue[self.front]

    def back_element(self) -> T:
        """
        Returns the element that self.back is indexing

        :return: The back element of the deque
        """
        if not self.is_empty():
            return self.queue[self.back]

    def enqueue(self, value: T, front: bool = True) -> None:
        """
        Adds a value to the front or back of the deque and grows the deque if it is full

        :param value: The value to add to the deque
        :param front: If True, add the value to the front of the deque, otherwise add it to the back.  Default is True
        """
        # If deque is empty
        if self.front is None and self.back is None:
            self.front = 0
            self.back = 0
            self.queue[self.front] = value

        # To the front
        elif front:
            self.front = (self.front - 1) % self.capacity
            self.queue[self.front] = value

        # To the back
        else:
            self.back = (self.back + 1) % self.capacity
            self.queue[self.back] = value

        self.size += 1
        # If deque is full
        if self.size == self.capacity:
            self.grow()
    def dequeue(self, front: bool = True) -> T:
        """
        Removes and returns a value from the front or back of the deque and shrinks the deque if it is 1/4 full
        and the capacity would be greater than 4 after shrinking.

        :param front: If True, remove the value from the front of the deque, otherwise remove it from the back.  Default is True
        :return: The value removed from the deque
        """
        # Ensures that you cannot dequeue from an empty deque
        if not self.is_empty():
            # Removes from the front
            if front:
                removed = self.queue[self.front]

                # If there is more than one element in the deque
                if self.front != self.back:
                    self.front = (self.front + 1) % self.capacity
                else:
                    self.front = None
                    self.back = None
            else:
                removed = self.queue[self.back]

                # If there is more than one element in the deque
                if self.front != self.back:
                    self.back = (self.back - 1) % self.capacity
                else:
                    self.front = None
                    self.back = None

            self.size -= 1

            # If the deque can be shrunk
            if self.size == self.capacity / 4 and self.capacity // 2 >= 4:
                 self.shrink()
            return removed
        return
    def grow(self) -> None:
        """
        Doubles the capacity of the deque and copies the elements to the new deque.  Overwrites the old deque with the new one.
        """
        new_queue = [None] * self.capacity * 2
        # temp_cap is to keep track of the old capacity since it my shrink from dequeue()
        temp_cap = self.capacity
        j = 0
        # dequeues all elements and adds them to the new deque
        while not self.is_empty():
            new_queue[j] = self.dequeue()
            j += 1
        self.front = 0
        self.back = j - 1
        self.size = j
        self.queue = new_queue
        self.capacity = temp_cap * 2


    def shrink(self) -> None:
        """
        Halves the capacity of the deque and copies the elements to the new deque.  Overwrites the old deque with the new one.
        """
        new_queue = [None] * (self.capacity // 2)
        # temp_cap is to keep track of the old capacity since it my shrink from dequeue()
        temp_cap = self.capacity
        j = 0
        # dequeues all elements and adds them to the new deque
        while not self.is_empty():
            new_queue[j] = self.dequeue()
            j += 1
        self.front = 0
        self.back = j - 1
        self.size = j
        self.queue = new_queue
        self.capacity = temp_cap // 2

def get_winning_numbers(numbers: List[int], size: int) -> List[int]:
    """
    INSERT DOCSTRINGS HERE!
    """
    window =  CircularDeque(data=numbers, capacity=len(numbers))
    window.front = 0
    window.back = size - 1

    max_list = []
    while window.back < window.capacity:
        max_list.append(max(window.queue[window.front:window.back + 1]))
        window.front += 1
        window.back += 1
    return max_list
    


def get_winning_probability(winning_numbers: List[int]) -> int:
    """
    INSERT DOCSTRINGS HERE!
    """
    even_path = winning_numbers[0::2]
    odd_path = winning_numbers[1::2]
    even_path_sum = sum(even_path)
    odd_path_sum = sum(odd_path)
    if even_path_sum > odd_path_sum:
        return even_path_sum
    return odd_path_sum


