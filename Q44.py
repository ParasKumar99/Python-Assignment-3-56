a = [10, 20, 30]

b = a.copy()
c = a

a.append(40)

print("Original list =", a)
print("Using copy() =", b)
print("Using assignment =", c)