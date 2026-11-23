a = [10, 20, 30, 40]
b = [30, 40, 50, 60]

common = []

for n in a:
    if n in b and n not in common:
        common.append(n)

print("Common elements =", common)