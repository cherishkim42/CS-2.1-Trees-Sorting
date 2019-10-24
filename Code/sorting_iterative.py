#!python

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so

    if len(items) <= 1: #empty array OR array with 1 item = already sorted
        return True
    
    for i in range(0, len(items)-1):
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
        for i in range(0, len(items)-1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]

    # """Here's what Nathan Pillai had:"""

    # index_1 = 0
    # index_2 = 1

    # while is_sorted(items) == False:

    #     if items[index_1] > items[index_2]:
    #         temp = items[index_1]
    #         items[index_1] = items[index_2]
    #         items[index_2] = temp

    #     index_1 += 1
    #     index_2 += 1

    # index_1 = 0
    # index_2 = 1


"""In process"""
def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    while is_sorted(items) is False:
        for i in range (0, len(items)-1):
            current_min = items[0] #first unsorted element
            if items[i] < current_min:
                current_min, items[i] = items[i], current_min

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
