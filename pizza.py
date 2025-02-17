import tabulate
import sys
from tabulate import tabulate
import csv

table = []
if len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit(1)
if len(sys.argv) < 2:
        print("Too few arguments")
        sys.exit(1)
if len(sys.argv) == 2:
    try:
        if sys.argv[1].endswith(".csv") == True:
            with open(sys.argv[1], "r") as file:
                lines = csv.reader(file)
                for row in lines:
                    table.append(row)
                print(tabulate(table, headers = "firstrow", tablefmt="grid"))
        else:
            print("Not a csv file")
            sys.exit(1)
    except:
        print("File does not exists")
        sys.exit(1)