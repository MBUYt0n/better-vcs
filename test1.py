with open("diff.txt", "r") as f:
    a = f.read().strip().split("||")[1:]
    f.close()

for i in a:
    b = i.split("\n")[2:]
    print(b)
