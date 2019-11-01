# Bubble sort example, O(n^2) efficiency estimate
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swapped = True
                # if num is greater, switch places with next num over
                arr[num], arr[num+1] = arr[num+1], arr[num]

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

bubble_sort(l)
# items should all be sorted now, END bubble sort
#Selection sort below ------------------------------------
def selection_sort(arr):
    # print("--- selection sorting ---")
    spot_marker = 0
    while spot_marker < len(arr):
        for num in range(spot_marker, len(arr)):
            if arr[num] < arr[spot_marker]:
                arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
        spot_marker += 1

l = [6,8,1,4,10,7,8,9,3,2,5]
selection_sort(l)

# insertion sort has a (On^2) complexity
# Insertion sort example ---------------------------

def insertion_sort(arr):
    for key in range(1, len(arr)):
        if arr[key] < arr[key-1]:
            j = key
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1

l = [6,1,8,4,10]
insertion_sort(l)
print(l)

#Merge sort below ---------------------------

def merge_sort(arr1, arr2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        i += 1
        j += 1
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        print(sorted_arr)
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

l1 = [2,4,6,8,10]
l2 = [1,2,3,7,8,9]


