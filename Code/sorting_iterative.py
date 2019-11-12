#!python

"""This file's sorting algorithms generally have quadratic time complexity"""

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so

    if len(items) <= 1: #empty array OR array with 1 item = already sorted
        return True
    
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            return False
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    
    while is_sorted(items) is False:
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    while is_sorted(items) is False:
        for i in range(len(items)):
            current_min = min(items[i:])
            index_min = items.index(current_min)
            items[i], items[index_min] = items[index_min], items[i]

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

    while is_sorted(items) is False:
        for i in range(len(items)):
            index = i
            current_element = items[i]
            while index > 0 and items[current_element - 1] > current_element:
                items[index] = items[index - 1]
                index -= 1
            items[index] = current_element



def nathan_bubble_sort(items):
    # Runtime: O(n), O(n^2) as worst case if the entire list is out of order, then we'd have to do bubble sort n times for (n) values in the list. Additional O(n) to check if sorted
    # Memory: O(1) because we just allocated memory for a couple variables.

    index_1 = 0
    index_2 = 1

    while is_sorted(items) == False:

        if items[index_1] > items[index_2]:
            temp = items[index_1]
            items[index_1] = items[index_2]
            items[index_2] = temp

        index_1 += 1
        index_2 += 1

    index_1 = 0
    index_2 = 1