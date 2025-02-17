import sys
import random

while True:
    try:
        i = int(input("Level: "))
        if i < 0:
            continue
        else:
            number = random.randint(0,i)
            while True:
                try:
                    j = int(input("Guess: "))
                    if j <0:
                        continue
                    elif j <number:
                        print("Too small!")
                        continue
                    elif j > number:
                        print("Too large!")
                        continue
                    elif j>i:
                        continue
                    else:
                        print("Just right!")
                        break
                except ValueError:
                    pass
            break
    except ValueError:
        pass