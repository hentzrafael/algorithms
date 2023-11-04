## Binary Search
It halves the number of items in a list after every iteration, resulting in much less iterations.

To get the number of iterations needed, we use the formula:

$log_2 n = x$ 

where $n$ is the size of a list or array, and $x$ is the number of iterations it will take to find the item, assuming the worst case scenario.

### Code in Python 3
First we need the list to be **ordered**, and after that, we can pass it as an argument to the function below:
```python
def binary_search(array:list, item:any) -> any:
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == item:
            return mid
        elif array[mid] < item:
            end = mid - 1
        elif array[mid] > item:
            start = mid + 1
    return None
```

## Exercises:
**1.1 - If you have a list with 128 ordered names and you want to perform a binary search on it. What is the maximum number of steps/iterations you will need?**

**R:** Using the formula, we have $log_2 128 = x $ , now we need to change $128$ to the base of $2$ using sucessive divisions of $2$. We then have $128 = 2^7$. Then we have $2^x = 2^7$, using the properties of potentiation, we have $x = 7$. The maximum number of iterations we could have is **$7$**.

**1.2 - Suppose you duplicate the number of names in the previous exercise list. How many iterations will it need now?**

**R:** We know that $128$ names need $7$ iterations. If we double it, we now have $256$ names on the list. We convert $256$ to base $2$ and we get $2^8$. This way, we can conclude that if we double the number of items, we only have one more iteration to find a value, and that is the advantage of using binary search.
