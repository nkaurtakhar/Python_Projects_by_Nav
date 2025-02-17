i = input("Input: ")

def main(i):
    v = ('a', 'e','i','o','u','A','E','I','O','U')
    for x in v:
            i = i.replace(x, "")
    return i

print("Output:", main(i))




