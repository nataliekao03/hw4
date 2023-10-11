def merge_list(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
            raise TypeError("Inputs both have to be lists")

    for item in list1 + list2:
        if not isinstance(item, int):
            raise TypeError("Input must contain only integers")

    i=0 
    j=0
    new_arr = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            new_arr.append(list1[i])
            i += 1
        else:
            new_arr.append(list2[j])
            j += 1

    if i < len(list1):
         while i < len(list1):
            new_arr.append(list1[i])
            i += 1

    else:
        while j < len(list2):
            new_arr.append(second[j])
            j += 1

    return new_arr