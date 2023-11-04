class BinarySearchList:
    def __init__(self) -> None:
        self.array = []
    
    """
    Searches for the index of an item in a sorted list.

    Parameters:
        item (any): The item to search for.

    Returns:
        any: The index of the item if found, None otherwise.
    """
    def binary_search(self, item:any) -> any:
        self.array.sort()
        start = 0
        end = len(self.array) - 1
        while start <= end:
            mid = (start + end) // 2
            if self.array[mid] == item:
                return mid
            elif self.array[mid] < item:
                end = mid - 1
            elif self.array[mid] > item:
                start = mid + 1
        return None

