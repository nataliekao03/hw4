def sort_dictionary(dict):
    keys = list(dict.keys())
    vals = list(dict.values())

    sorted = []
    i = 0
    j = 0
    smallest = 0

    while i < len(dict):
        while j < len(keys):
            if vals[smallest][1] > vals[j][1]:
                smallest = j
            
            j += 1
        sorted.append((keys[smallest], vals[smallest][0]))
        del keys[smallest]
        del vals[smallest]
        i += 1
        smallest = 0
    
    return sorted