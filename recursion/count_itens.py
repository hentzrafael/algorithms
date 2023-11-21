def count_itens(arr:list) -> int:
    if  arr == []:
        return 0
    return 1 + count_itens(arr[1:])

