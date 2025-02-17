import sys
from PIL import Image

if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
if len(sys.argv) == 3:
    extensions = [".jpg",".jpeg",".png"]
    for x in extensions:
        if sys.argv[1].endswith(x) == sys.argv[2].endswith(x):
            try:
                file1 = Image.open(sys.argv[1])

            except FileNotFoundError:
                sys.exit("File not found")

            file2 = Image.open("shirt.png")
            size = file2.size
            muppet = ImageOps.fit(file1, size)
            muppet.paste(file2, file2)

        else:
            sys.exit(1)




