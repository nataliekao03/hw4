def sort_dictionary(input_dict):
    sorted_list = sorted(input_dict.items(), key=lambda item: item[1][1], reverse=True)
    result = [(name, data[0] for name, data in sorted_list)]
    return result