def selection_sort_with_swap_count(arr):
    n = len(arr)
    count_swap = 0

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:  # Only swap if min_index is different from i
            arr[i], arr[min_index] = arr[min_index], arr[i]
            count_swap += 1

    return arr, count_swap

# Example usage
List = [6, 8, 19, 48, 9, 90]
sorted_list, swaps = selection_sort_with_swap_count(List)

print("Sorted List:", sorted_list)
print("Number of swaps:", swaps)