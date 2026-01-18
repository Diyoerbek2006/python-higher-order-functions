prices = ["$120", "$340", "$50", "$90"]
numbers = list(map(lambda p: int(p.replace("$", "")), prices))
print(numbers)
