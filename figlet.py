import sys
from pyfiglet import Figlet
figlet = Figlet()

fonts = figlet.getFonts()
if len(sys.argv) == 1:
    i = input("Input: ")
    print("Output:", figlet.renderText(i))

elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fonts:
    i = input("Input: ")
    figlet.setFont(font=(sys.argv[2]))
    print("Output:", figlet.renderText(i))
else:
    sys.exit("Invalid usage")


