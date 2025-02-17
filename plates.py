def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    x = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    Y = ('0123456789')
    def twostr():
        for i in s[0:2]:
            if i[0:2] in x:
                return True
            else:
                return False
    def leng():
        if len(s)>=2 and len(s) <= 6:
            return True
    def num():
        for c in s:
            if c.isdigit():
                j = s.index(c)
                if s[j:].isdigit() and c != '0':
                    return True
                else:
                    return False
                




    if twostr() and leng() == True and num() == True:
        return True


    '''if s[0:2] in x:
        return True
    if 2<=len(s)>=6:
        return True'''




main()
