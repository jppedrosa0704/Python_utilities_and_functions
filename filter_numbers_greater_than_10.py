# Filter only numbers greater than 10.
numbers = [5, 12, 7, 20, 3, 15]

numbers_greater_than_10 = list(filter(
    lambda n: n > 10, numbers)
)
print(numbers_greater_than_10)