x = input("Greeting: ").lower().strip()
if x.startswith("hello"):
    print("$0")
elif x.startswith("h") and x != "hello":
    print("$20")
else:
    print("$100")