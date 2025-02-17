Amount = 50
while True:
    print("Amount Due:", Amount)
    i = int(input("Insert Coin: "))
    if i < Amount and i in [25,10,5]:
        Amount = int(Amount) - int(i)
    elif i not in [25,10,5]:
        continue
    else:
        A = i - Amount
        print("Change Owed:", A)
        break







