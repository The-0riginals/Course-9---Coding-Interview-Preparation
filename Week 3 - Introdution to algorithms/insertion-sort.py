def insertion_sort_with_swap_count(arr):
    n = len(arr)
    count_swap = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            count_swap += 1

        arr[j + 1] = key

    return arr, count_swap

# Example usage
List = [6, 8, 19, 48, 9, 90]
sorted_list, swaps = insertion_sort_with_swap_count(List)

print("Sorted List:", sorted_list)
print("Number of swaps:", swaps)