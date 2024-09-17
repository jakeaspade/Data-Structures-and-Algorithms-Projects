"""
Project 2 - Hybrid Sorting
CSE 331 Fall 2024
"""

from typing import TypeVar, List, Callable

T = TypeVar("T")  # represents generic type


# This is an optional helper function but HIGHLY recommended, especially for the application problem!
def do_comparison(first: T, second: T, comparator: Callable[[T, T], bool], descending: bool) -> bool:
    """
    FILL OUT DOCSTRING
    """
    pass


def selection_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    FILL OUT DOCSTRING
    """
    pass


def bubble_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                descending: bool = False) -> None:
    """
    FILL OUT DOCSTRING
    """
    pass


def insertion_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    FILL OUT DOCSTRING
    """
    pass


def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    FILL OUT DOCSTRING
    """
    pass


def quicksort(data: List[T]) -> None:
    """
    Sorts a list in place using quicksort
    :param data: Data to sort
    """

    def quicksort_inner(first: int, last: int) -> None:
        """
        Sorts portion of list at indices in interval [first, last] using quicksort

        :param first: first index of portion of data to sort
        :param last: last index of portion of data to sort
        """
        # List must already be sorted in this case
        if first >= last:
            return

        left = first
        right = last

        # Need to start by getting median of 3 to use for pivot
        # We can do this by sorting the first, middle, and last elements
        midpoint = (right - left) // 2 + left
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]
        if data[left] > data[midpoint]:
            data[left], data[midpoint] = data[midpoint], data[left]
        if data[midpoint] > data[right]:
            data[midpoint], data[right] = data[right], data[midpoint]
        # data[midpoint] now contains the median of first, last, and middle elements
        pivot = data[midpoint]
        # First and last elements are already on right side of pivot since they are sorted
        left += 1
        right -= 1

        # Move pointers until they cross
        while left <= right:
            # Move left and right pointers until they cross or reach values which could be swapped
            # Anything < pivot must move to left side, anything > pivot must move to right side
            #
            # Not allowing one pointer to stop moving when it reached the pivot (data[left/right] == pivot)
            # could cause one pointer to move all the way to one side in the pathological case of the pivot being
            # the min or max element, leading to infinitely calling the inner function on the same indices without
            # ever swapping
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1

            # Swap, but only if pointers haven't crossed
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        quicksort_inner(first, left - 1)
        quicksort_inner(left, last)

    # Perform sort in the inner function
    quicksort_inner(0, len(data) - 1)


###########################################################
# DO NOT MODIFY
###########################################################
class Product:
    """
    Class that represents products.
    """
    __slots__ = ['price', 'rating', 'relevance']

    def __init__(self, price: float, rating: int, relevance: float) -> None:
        """
        Constructor for the Product class.

        :param price: The price of the product.
        :param rating: The rating of the product.
        :param relevance: A score representing how closely the product matches the user's search keywords. A higher value
        indicates a stronger match between the product and the search query.
        :return: None
        """
        self.price = price
        self.rating = rating
        self.relevance = relevance

    def __repr__(self) -> str:
        """
        Represent the Product as a string.

        :return: Representation of the product.
        """
        return str(self)

    def __str__(self) -> str:
        """
        Convert the Product to a string.

        :return: String representation of the product.
        """
        return f'<price: {self.price}, rating: {self.rating}, relevance: {self.relevance}>'

    def __eq__(self, other) -> bool:
        """
        Compare two Product objects for equality based on price and rating.

        :param other: The other Product to compare with.
        :return: True if products are equal, False otherwise.
        """
        return self.price == other.price and self.rating == other.rating and self.relevance == other.relevance


###########################################################
# MODIFY BELOW
###########################################################
def recommend_products(products: List[Product], sorted_by: str) -> List[Product]:
    """
    FILL OUT DOCSTRING.
    """
