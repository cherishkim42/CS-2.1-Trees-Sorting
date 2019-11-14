#!python
from sorting_iterative import bubble_sort, selection_sort, insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a 🌟NEW🌟 list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty ✅
    # TODO: Find minimum item in both lists and append it to new list ✅
    # TODO: Append remaining items in non-empty list to new list ✅
    return_list = []
    while len(items1) > 0 and len(items2) > 0:
        if items1[0] < items2[0]:
            return_list.append[items1.pop(0)]
        else:
            return_list.append[items2.pop(0)]
    else:
        if len(items1) == 0 and len(items2) > 0:
            for item in items2:
                return_list.append(item)
        elif len(items1) > 0 and len(items2) == 0:
            for item in items1:
                return_list.append(item)
    return return_list

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order
    center = len(items) // 2
    left = selection_sort(items[:center])
    right = selection_sort(items[center:])
    merged_items = merge(left, right)

    for i in range(len(items)):
        items[i] = merged_items[i]
    return items

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each 🌟recursively🌟, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) < 2:
        return items
    center = len(items) // 2
    left = merge_sort(items[:center])
    right = merge_sort(items[center:])
    merged_items = merge(left, right)

    items[:] = merged_items #mutates items to contain each and every indexed item in merged_items - as opposed to 'items = merged_items', which would simply assign merged_items to the items VARIABLE without actually altering 'items' itself
    return items

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pivot_index = low #set pivot
    swap_index = pivot_index + 1
    for index in range(low+1, high): #traverse array
        if items[index] < items[pivot_index]:
            items[index], items[pivot_index] = items[pivot_index], items[index]
            swap_index += 1
    items[pivot], items[swap_index-1] = items[swap_index-1], items[pivot]
    return(swap_index-1)

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    if low is None:
        low = 0
    if high is None:
        high = len(items)-1

    # TODO: Check if list or range is so small it's already sorted (base case)
    # if len(items) < 2: #rather than 'len(items)' it should be based on low and high due to this fxn being done IN PLACE
    #     return items
    if ((high-low)+1) < 2: #because high=len(items)-1, ex. a list with items of index 0 and 1 is a list of len 2
        return
    
    # TODO: Partition items in-place around a pivot and get index of pivot
    pivot = partition(items, low, high)

    # TODO: Sort each sublist range by recursively calling quick sort. REMEMBER TO EXCLUDE THE PIVOT ITSELF
    left = quick_sort(items, low, pivot-1)
    right = quick_sort(items, pivot+1, high)

   # divide:
       # select a pivot to compare items to
       # partition all items into 2 groups
           # items <= pivot
           # items > pivot
       # [5, 2, 8, 7, 1, 9, 3] pivot: 5
           # [2, 1, 3] and [8, 7, 9]
   # conquer:
       # sort the two groups with quick sort recursively
   # combine:
       # concatenate lesser group, pivot, greater group
       # list1 + pivot + list2
       # [1, 2, 3] + [5] + [7, 8, 9]
