import sys
import csv

table = []
if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
if len(sys.argv) == 3:
    try:
            output = []
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    y, x = row["name"].split(",")
                    z = row["house"]
                    output.append({'first': x.lstrip(),'last':y, 'house':z})
                with open(sys.argv[2], "w") as file2:
                    writer = csv.DictWriter(file2, fieldnames = ["first", "last", "house"])
                    writer.writeheader()
                    for row in output:
                        writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})

    except:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)