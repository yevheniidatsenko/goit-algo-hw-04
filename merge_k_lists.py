def merge_k_lists(lists):
    merged_list = []
    lists_iter = [iter(lst) for lst in lists]
    current_values = [(next(it, None), i) for i, it in enumerate(lists_iter)]
    current_values = [x for x in current_values if x[0] is not None]

    while current_values:
        min_val, min_ind = min(current_values, key=lambda x: x[0])
        merged_list.append(min_val)
        next_val = next(lists_iter[min_ind], None)
        if next_val is not None:
            current_values[current_values.index((min_val, min_ind))] = (next_val, min_ind)
        else:
            current_values.remove((min_val, min_ind))

    return merged_list

lists = [[1, 1, 2], [1, 3, 4], [4, 4, 5, 6]]
print("Відсортований список:", merge_k_lists(lists))