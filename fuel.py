while True:
        try:
            i = (input("Fraction: "))
            x,y = (i.split(sep="/"))
            if type(x) == int and type(y) == int:
                x = int(x)
                y = int(y)
                r = round(((x/y)*100))
            else:
                raise Exception
            if x>y:
                continue
            if r<=1:
                print("E")
                break
            elif r >=99:
                print("F")
                break

            else:
                print(f"{r}%")
                break


        except (ValueError, ZeroDivisionError):
            continue

