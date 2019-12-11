#!python

# This file's sorting algorithms generally have quadratic time complexity

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) where n = length of 'items' b/c you gotta check em all
    Memory usage: O(1). This function returns a boolean and stores nothing"""
    
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            return False
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: [BEST] O(n) if already sorted; [WORST & common] O(n^2) unsorted;
    Memory usage: O(1). Param list changed, no new list; no new memory needs allocation"""
    
    while is_sorted(items) is False:
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
    return items

def selection_sort(items): #Anisha suggests no while loop
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) due to 2 nested for loops
    Memory usage: O(1). Param list changed, no new list; no new memory needs allocation"""

    for i in range(len(items)):
        min_index = i
        for j in range(i, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        items[min_index], items[i] = items[i], items[min_index]
    return items

def insertion_sort(items): #Anisha suggests no while loop
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: [BEST] O(n), only 1 unsorted item needs to be moved. [WORST] O(n^2) due to 2 nested for loops
    Memory usage: O(1). Param list changed, no new list; no new memory needs allocation"""

    for i in range(len(items)):
        sort_me = items[i]
        next_index = i - 1
        if items[next_index] > sort_me and next_index >= 0:
            items[next_index + 1] = items[next_index]
            next_index -= 1
        items[next_index + 1] = sort_me
    return items

 






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