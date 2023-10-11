def sort_dictionary(dict):
    keys = list(dict.keys())
    vals = list(dict.values())

    sorted = []
    i = 0
    j = 0

    while i < len(dict):
        greatest = 0
        while j < len(keys):
            if vals[j][1] > vals[greatest][1]:
                greatest = j
            
            j += 1
        sorted.append((keys[greatest], vals[greatest]))
        del keys[greatest]
        del vals[greatest]
        i += 1
        greatest = 0
    
    return sorted