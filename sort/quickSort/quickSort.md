# QuickSort Algorithm

The QuickSort algorithm is a divide-and-conquer sorting algorithm that works by selecting a pivot element and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted.

## Algorithm Steps

1. Choose a pivot element from the array. This can be done randomly or by selecting the first, middle, or last element of the array.

2. Partition the array into two sub-arrays:
   - Elements smaller than the pivot go to the left sub-array.
   - Elements greater than the pivot go to the right sub-array.

3. Recursively apply the above steps to the left and right sub-arrays until the sub-arrays have only one element.

4. Concatenate the sorted left sub-array, the pivot element, and the sorted right sub-array to get the final sorted array.

## Implementation in Python
```python
def quick_sort(arr : list) -> list:
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1::] if i <= pivot]
    greater = [i for i in arr[1::] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

```

## Big O Notation
In the medium case scenario, Quick Sort will have $O(n * log *n)$, because it will iterate over each sub-array.
In the worst case scenario, it will have $O(n²)$ time complexity.

But we consider QuickSort as $O(n * log *n)$ complexity, because the algorithm itself works more frequently at the medium case scenario.
