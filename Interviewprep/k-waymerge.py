import heapq
#Time Complexity: O(N log k) where N is the total number of elements and k is the number of lists
# Space Complexity: O(k) for the heap
def merge_two_sorted_lists(list1, list2):
    """Merge two sorted lists into a single sorted list.

    Args:
        list1 (List[int]): First sorted list.
        list2 (List[int]): Second sorted list.

    Returns:
        List[int]: A single merged and sorted list.
    """
    merged = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append any remaining elements from either list
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged
#Time Complexity: O(N log k) where N is the total number of elements and k is the number of lists
# Space Complexity: O(1) if we don't count the output list
def pairwise_merge(lists):
    """Merge multiple sorted lists into a single sorted list using pairwise merging.

    Args:
        lists (List[List[int]]): A list of sorted lists.

    Returns:
        List[int]: A single merged and sorted list.
    """
    if not lists:
        return []

    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged_lists.append(merge_two_sorted_lists(lists[i], lists[i + 1]))
            else:
                merged_lists.append(lists[i])
        lists = merged_lists

    return lists[0]
#Time Complexity: O(N log k) where N is the total number of elements and k is the number of lists
# Space Complexity: O(k) for the heap
def k_way_merge(sorted_lists):
    """Merge k sorted lists into a single sorted list.

    Args:
        sorted_lists (List[List[int]]): A list of k sorted lists.

    Returns:
        List[int]: A single merged and sorted list.
    """
    min_heap = []
    result = []

    # Initialize the heap with the first element of each list
    for i, lst in enumerate(sorted_lists):
        if lst:  # Ensure the list is not empty
            heapq.heappush(min_heap, (lst[0], i, 0))  # (value, list_index, element_index)

    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        result.append(value)

        # If there is a next element in the same list, add it to the heap
        if element_index + 1 < len(sorted_lists[list_index]):
            next_value = sorted_lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return result

lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# merged_list = k_way_merge(lists)
# merge_two_sorted_lists = pairwise_merge(lists)
print(merge_two_sorted_lists)  # Output: [1, 2, 3,
