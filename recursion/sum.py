def sum_array(arr : list) -> int:
    if arr == []:
        return 0
    return arr[0] + sum_array(arr[1:])


