import sys

num = 0
for arg in sys.argv[1: ]:
    if arg.endswith(".py") == False:
        print("Not a Python file")
        sys.exit()
    else:
        try:
            file = open(arg, "r")
            lines = file.readlines()
            for count, line in enumerate(lines):
                pass
            num = count + 1
            comment = lines.startswith("#")
            emptyline = ""

            print(num)


        except FileNotFoundError:
            print("File does not exist")