def sort_dictionary(input_dict):
    keys = list(input_dict.keys())
    vals = list(input_dict.values())

    sorted_list = []
    i = 0

    while i < len(input_dict):
        greatest = 0
        j = 0

        while j < len(keys):
            if vals[j][1] >= vals[greatest][1]:
                greatest = j

            j += 1

        sorted_list.append(
            (keys[greatest], vals[greatest][0])
        )  # Access the phone number (first element of the tuple)
        keys.pop(greatest)
        vals.pop(greatest)
        i += 1

    return sorted_list
