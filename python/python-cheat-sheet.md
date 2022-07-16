# Python Cheat Sheet

## Inputs
```python
name = input("What is your name: ")
print(f'Hello {name}')
```

## Functions
```python
def add_two_numbers(a, b):
    """
    Add two numbers a and b
    Input: int a, int b
    Output: a + b
    """
    return a + b

# print docstring
print(add_two_numbers.__doc__)
```