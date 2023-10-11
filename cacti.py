def cacti_number(arr):
    counter = 0
    available = True
    row = len(arr)
    cols = len(arr[0])

    for i in range(row):
        for j in range(cols):
            if arr[i][j] == 1:
                available = False
            elif (
                i > 0 and arr[i - 1][j] == 1
            ):  # checks for adjacent cacti horizontally and veritcally
                available = False
            elif i < row - 1 and arr[i + 1][j] == 1:
                available = False
            elif j > 0 and arr[i][j - 1] == 1:
                available = False
            elif j < cols - 1 and arr[i][j + 1] == 1:
                available = False

            if available:
                arr[i][j] = 1
                counter += 1

            available = True

    return counter
