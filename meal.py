def main():
    x = input("What time is it? ")
    y = convert(x)
    if 7.00 <= y <= 8.00:
        print("breakfast time")
    elif 12.00 <= y <= 13.00:
        print("lunch time")
    elif 18.00 <= y <= 19.00:
        print("dinner time")
    else:
        pass



def convert(time):
    h, m = time.split(":")
    m = float(m) * 1/60
    return float(h) + m


main()

