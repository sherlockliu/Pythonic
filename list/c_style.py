list = []
for i in range(10):
    if i % 2 == 0:
        list.append(i)

print(list)

print([i for i in range(10) if i % 2 == 0])

for i, el in enumerate(list):
    print(f"{i} is {el}")
