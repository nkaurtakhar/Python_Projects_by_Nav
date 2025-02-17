x = {}
while True:

    try:
        i = input()

        if i in x:
            x[i] +=1
        else:
            x[i] = 1


    except EOFError:
        for y in sorted(x.keys()):

            print(x[y], y.upper())
        break

