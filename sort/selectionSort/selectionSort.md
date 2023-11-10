## Selection Sort
Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the remaining part of the array and placing it at the end. It continues doing this until the entire array is sorted.

### Algorithm
1. Start with the first unsorted array.
2. Compare this element with all the elements to its right.
3. Add the minimum element to the new sorted array.
4. Remove from the unsorted array the added element.
5. Repeat until the array is sorted.

### Example
```python
def min_index(array:list) -> any:
        less = array[0]
        less_index = 0
        for index in range(1, len(array)):
            if less > array[index]:
                less = array[index]
                less_index = index
        return less_index

    def selection_sort(array:list) -> list:
        sorted_array = []
        for i in range(len(array)):
            sorted_array.append(array.pop(self.min_index(array)))
        return sorted_array 
```

### Complexity
Time complexity: $O(n^2)$, where n is the number of elements in the array.