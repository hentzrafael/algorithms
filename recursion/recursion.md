## Recursion

Recursion is a programming concept where a function calls itself repeatedly until a base condition is met. It allows solving complex problems by breaking them down into smaller, more manageable sub-problems.

### How it works?

1. The function checks if the base condition is met. If so, it returns a specific result. The base condition usually is the stop condition for the recursion.

2. If the base condition is not met, the function calls itself again with a modified input or parameters.

3. The function continues to call itself until the base condition is met, forming a call stack.

4. Once the base condition is met, the function starts returning results from the deepest level of the call stack, unraveling the recursion.

Recursion can be a powerful technique for solving problems that can be divided into smaller identical or similar sub-problems. However, it's important to define the base condition properly to avoid infinite recursion.

### Example of recursion in Python 3
```python
    def factorial(n : int) -> int:
    if n == 1: #Base Condition
        return 1
    
    return n * factorial(n - 1) #Call itself
```