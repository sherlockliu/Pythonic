# ！/usr/bin/python


def not_a_generator(max_range: int) -> list:
    result = []
    for r in range(max_range):
        result.append(r)
    return result


def generator(max_range: int):
    for r in range(max_range):
        yield r


g = generator(3)

print(g.__next__())
print(g.__next__())
print(g.__next__())
