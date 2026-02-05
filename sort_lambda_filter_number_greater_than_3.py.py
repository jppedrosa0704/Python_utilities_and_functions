numbers = [3, 6, 9, 12, 15, 18, 2, 5, 7]

n = list(sorted(filter(lambda d: d>10 and d % 3 == 0, numbers)))

print(n)

# list comprehension:

d = [d for d in numbers if d > 10 and d % 3 == 0]
print(d)