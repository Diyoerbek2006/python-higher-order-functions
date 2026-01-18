nums = list(range(1, 21))

juftlar_kvadrati = list(
    map(lambda x: x * x,
        filter(lambda x: x % 2 == 0, nums))
)

print(juftlar_kvadrati)
