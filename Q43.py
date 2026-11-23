a = [10, 20, 30, 40, 50]

n = int(input("Enter element: "))

if n in a:
    print("Index =", a.index(n))
else:
    print("Element not found")