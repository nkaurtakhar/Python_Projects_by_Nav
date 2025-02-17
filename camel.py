x = input("camelCase: ")
def snake(x):
    y = [x[0].lower()]
    for i in x[1:]:
        if i in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            y.append('_')
            y.append(i.lower())
        else:
            y.append(i)
    return ''.join(y)

print("Snake_Case: " + snake(x))