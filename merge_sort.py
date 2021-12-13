a = [27,3,-91,2,99,52,1,-10]

def merge_sort(lst):
    # Base case: A 1- or 0-element list is already sorted
    # If we encounter one, return it immediately
    if len(lst) <= 1:
        return lst[:]

    # Find the midpoint of the list
    midpt = int(len(lst) / 2)

    # Create left and right halves from the midpoint
    left = lst[:midpt]
    right = lst[midpt:]

    # Recursively merge sort both the left and right halves.
    # Once these calls return, new_left and new_right are
    # guaranteed to be in sorted order.
    new_left = merge_sort(left)
    new_right = merge_sort(right)

    # Create a new list to merge the contents of new_left and new_right
    new_lst = []

    # Merge operation: Copy the elements of new_left and new_right
    # into the merged array so they are in order
    i = 0
    j = 0
    while i < len(new_left) and j < len(new_right):
        if new_left[i] < new_right[j]:
            new_lst.append(new_left[i])
            i += 1
        else:
            new_lst.append(new_right[j])
            j += 1
    
    # Clean-up step: either new_left or new_right are
    # likely to have leftover elements. If so, add them.
    if i < len(new_left):
        for x in range(i, len(new_left)):
            new_lst.append(new_left[x])
    elif j < len(new_right):
        for y in range(j, len(new_right)):
            new_lst.append(new_right[y])

    # new_lst is now sorted. Return it.
    return new_lst

print(a)
print(merge_sort(a))