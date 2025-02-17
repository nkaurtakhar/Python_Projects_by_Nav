import sys
import random


def main():
    level = get_level()
    print("Score:" , ten_count(level))



def get_level():
    while True:
        try:
            level = int(input("level: "))
            if level == 1 or level ==2 or level ==3 :
                break
        except:
            pass
    return level



def generate_integer(level):

    if level == 1:
        a = random.randint(0,9)
        b = random.randint(0,9)
    elif level == 2:
        a = random.randint(10,99)
        b = random.randint(10,99)
    elif level == 3:
        a = random.randint(100,999)
        b = random.randint(100,999)

    return a,b


def Three_tries(a,b):
    tries= 1
    while tries <=3:
        try:
            i = int(input(f"{a} + {b} = "))
            if i == a + b:
                return True
            else:
                print("EEE")
                tries = tries +1

        except:
            tries += 1
            print("EEE")
            
    print(f"{a} + {b} = {a+b}")
    return False

def ten_count(level):
    count = 1
    score = 0
    while count <=10:
        a,b = generate_integer(level)
        if Three_tries(a,b) == True:
            score += 1
        count += 1
    return score







if __name__ == "__main__":
    main()