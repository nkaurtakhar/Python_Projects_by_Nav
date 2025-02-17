import sys
import inflect

p = inflect.engine()
k = []
while True:
    try:
        i = input("Name: ")
        k.append(i)
        continue
    except EOFError:
        print()
        x= p.join(k)
        print("Adieu, adieu, to", x)
        sys.exit()
