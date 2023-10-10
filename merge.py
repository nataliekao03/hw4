def merge_list(list1, list2):
    if not(isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Inputs should be lists")
    
    for item in list1 + list2:
        if not isinstance(item, int):
            raise TypeError("Inputs can only contain integers")
    
    new_arr = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            new_arr.append(list1[i])
            i += 1
        else:
            new_arr.append(list2[j])
            j += 1

    new_arr.extend(list1[i: ])
    new_arr.extend(list2[j: ])

    return new_arr




    