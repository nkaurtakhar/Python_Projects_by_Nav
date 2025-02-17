i = input("Expression: ")
x, y, z = i.split(" ")
if y == "+":
    p = int(x) + int(z)
elif y == "-":
    p = int(x) - int(z)
elif y == "/":
    p = int(x) / int(z)
elif y == "*":
    p = int(x) * int(z)

print(round(float(p),1))
