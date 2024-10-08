"""
Project 2 - Hybrid Sorting
CSE 331 Fall 2024
"""
from msvcrt import kbhit
from typing import TypeVar, List, Callable

T = TypeVar("T")  # represents generic type


# This is an optional helper function but HIGHLY recommended, especially for the application problem!
def do_comparison(first: T, second: T, comparator: Callable[[T, T], bool], descending: bool) -> bool:
    """
    Does the comparison between two elements based on the comparator criteria used by the sorting function
        and the returns the result based on the descending boolean.

    :param first: The first element to compare
    :param second: The second element to compare
    :param comparator: The function to use to compare the two elements
    :param descending: A boolean that indicates whether the comparison should be in descending order
    :return: A boolean that indicates whether the comparison is True or False

    """
    decision = comparator(first,second)
    if descending:
        return not decision
    else:
        return decision

def selection_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    This sort starts at the beginning of a list and finds the minimum of the list from data[i:].  After finding
    the min_index, the elements of i and min_index are swapped, effectively putting the minimum value at the beginning
    of the unsorted part of the list.

    :param data: The list to sort
    :param comparator: The function to use to compare the two elements
    :param descending: A boolean that indicates whether the comparison should be in descending order
    :return: None
    """
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if do_comparison(data[j],data[min_index],comparator,descending):
                min_index = j
        data[i],data[min_index] = data[min_index],data[i]


def bubble_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                descending: bool = False) -> None:
    """
    This sort compares adjacent elements and swaps them if they are in the wrong order.  This process is repeated
    until the list is sorted.

    :param data: The list to sort
    :param comparator: The function to use to compare the two elements
    :param descending: A boolean that indicates whether the comparison should be in descending order
    :return: None
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(data)):
            if do_comparison(data[i], data[i - 1], comparator, descending):
                data[i], data[i - 1] = data[i - 1], data[i]
                swapped = True


def insertion_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    This sort builds the final sorted list one element at a time.  It takes the first element and skips it, then for every
    number after the first element, it inserts the number into the correct position in the sorted part of the list.
    The sorted part of the list is always the first i elements of the list.

    :param data: The list to sort
    :param comparator: The function to use to compare the two elements
    :param descending: A boolean that indicates whether the comparison should be in descending order
    :return: None
    """
    for i in range(len(data)):
        if i == 0:
            continue
        temp = data[i]
        data.pop(i)
        insert_index = i
        j = i
        while j >= 1:
            if do_comparison(temp, data[j-1], comparator, descending):
                insert_index -= 1
                j -= 1
            else:
                break
        data.insert(insert_index, temp)


def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    This sort is a hybrid of merge and insertion sorts.  It uses insertion sort for small lists and merge sort for
    larger lists.  The threshold parameter determines the size of the list that will be sorted using insertion sort.
    This sort is also capable of using only merge sort if the threshold is set to 0.

    :param data: The list to sort
    :param threshold: The size of the list that will be sorted using insertion sort
    :param comparator: The function to use to compare the two elements
    :param descending: A boolean that indicates whether the comparison should be in descending order
    :return: None
    """
    # True merge sort (no insertion)
    if threshold == 0:
        if len(data) == 1:
            return
    # Hybrid merge sort (uses insertion at a threshold)
    if len(data) <= threshold:
        insertion_sort(data=data, comparator=comparator, descending=descending)

    else:
        left_part = data[:len(data)//2]
        right_part = data[len(data)//2:]
        hybrid_merge_sort(data=left_part, threshold=threshold, comparator=comparator, descending=descending)
        hybrid_merge_sort(data=right_part, threshold=threshold, comparator=comparator, descending=descending)
        k = 0
        while len(left_part) > 0 and len(right_part) > 0:
            if do_comparison(left_part[0], right_part[0], comparator, descending):
                data[k] = left_part[0]
                left_part.pop(0)
            else:
                data[k] = right_part[0]
                right_part.pop(0)
            k += 1
       # In case of len(left_part) != len(right_part)

        # Merge remaining left part if there are more remaining
        for num in left_part:
            data[k] = num
            k += 1
        # Merge remaining right part if there are more remaining
        for num in right_part:
            data[k] = num
            k += 1


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
    Given a list of products and a sorting criteria, return a list of recommended products sorted by the sorting criteria.

    :param products: A list of products to recommend
    :param sorted_by: A string that specifies the sorting criteria. It can be one of the following:
        - 'price_low_to_high': Sort products by price in ascending order
        - 'price_high_to_low': Sort products by price in descending order
        - 'rating': Sort products by rating in descending order
    :return: A list of recommended products sorted by the sorting criteria
    """
    sorted = products
    hybrid_merge_sort(data=sorted, comparator=lambda x,y: x.relevance > y.relevance)
    sorted = sorted[:round(len(sorted) * .3)]

    if sorted_by == 'price_low_to_high':
        hybrid_merge_sort(data=sorted, comparator=lambda x, y: x.price < y.price if x.price!=y.price else x.rating>y.rating, descending=False)
    if sorted_by == 'price_high_to_low':
        hybrid_merge_sort(data=sorted, comparator=lambda x, y: x.price > y.price if x.price!=y.price else x.rating>y.rating, descending=False)
    if sorted_by == 'rating':
        hybrid_merge_sort(data=sorted, comparator=lambda x, y: x.rating > y.rating if x.rating!=y.rating else x.price<y.price, descending=False)
    return sorted