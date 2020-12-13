a = int(input())
b = int(input())

count = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i)
        count = count + 1

print(count)


# range(14)        # [0, 1, 2, ..., 14]
# range(6, 14)     # [5, 6, ..., 14]
# range(6, 14, 2)  # [5, 7, 9, 11, 13]