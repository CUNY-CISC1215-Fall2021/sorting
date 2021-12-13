a = [3, 27, -91, 2, 99, 52]

def sort(lst):
    # Variable to track whether we perform any swaps this iteration
    swapped = True

    while(swapped):
        swapped = False

        # Iterate through every element in the list
        for i in range(len(a)-1):

            # If the current element is greater than the next element, we swap them
            if a[i] > a[i+1]:
                swapped = True
                tmp = a[i]
                a[i] = a[i+1]
                a[i+1] = tmp

print(a)
sort(a)
print(a)