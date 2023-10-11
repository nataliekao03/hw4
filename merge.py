def merge_list(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Inputs both have to be lists")

    for item in list1 + list2:
        if not isinstance(item, int):
            raise TypeError("Input must contain only integers")

    merged_list = list1 + list2

    for i in range(len(merged_list)):
        for j in range(i, len(merged_list)):
            if merged_list[i] > merged_list[j]:
                merged_list[i], merged_list[j] = merged_list[j], merged_list[i]

    return merged_list
