#sort list of tuples

data = [("Ana", 23), ("Bruno", 19), ("Carlos", 30)]

data.sort(key=lambda d: d[1])
print(data)

