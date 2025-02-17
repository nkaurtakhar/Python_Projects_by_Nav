j = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

while True:
    i = input("Date: ").strip()
    try:
            month,day,year = (i.split(sep="/"))
            day,month = int(day), int(month)
            if 0<month<=12 and 0<day<=31:
                new_month = int(month)
                new_day = int(day)
                break
    except:
        try:
            month,day,year = (i.split(sep=" "))
                #day,month = int(day), (month)
                #if 0<month<=12 and 0<day<=31:
            if "," in i[0:]:
                for l in range(len(j)) :
                    if month == j[l]:
                        new_month= l +1
                new_day = day.replace(",","")
                new_day = int(new_day)
                new_month = int(new_month)
                if 0<new_month<=12 and 0<new_day<=31:
                    break

        except:
            print()
            pass

print(f"{year:04}-{new_month:02}-{new_day:02}")


