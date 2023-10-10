def merge_list(list1, list2):
    newList = list1 + list2
    newList.sort()  # n log n
    return newList
