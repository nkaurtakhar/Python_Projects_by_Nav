x = input("File name: ").strip().lower()
if x.endswith(".gif"):
    print("image/gif")
elif x.endswith(".jpg" or ".jpeg"):
    print("image/jpeg")
elif x.endswith(".png"):
    print("image/png")
elif x.endswith(".pdf"):
    print("application/pdf")
elif x.endswith(".txt"):
    print("txt/plain")
elif x.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")