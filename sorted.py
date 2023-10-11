def sort_dictionary(dict):
    keys = list(dict.keys())
    vals = list(dict.values())

    sorted = []
    i = 0
    j = 0
    greatest = 0

    while i < len(dict):
        while j < len(keys):
            if vals[j][1] > vals[greatest][1]:
                greatest = j
            
            j += 1
        sorted.append((keys[greatest], vals[greatest][0]))
        keys.pop(greatest)   
        vals.pop(greatest)   
        i += 1
    
    return sorted