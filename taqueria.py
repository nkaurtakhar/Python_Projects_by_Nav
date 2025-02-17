d = {
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
            }
x = 0
while True:
    try:
        item = input("Item: ").title()
        if item == "Control-D":
            break
        def main(c):
            if c in d:
                total = d[c]
                return total
        x = main(item) + x
        print("Total:","${:.2f}".format(x))

    except (EOFError):
        print()
        break

    except (KeyError, TypeError):
        pass
