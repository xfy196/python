f = open("new_file.txt", "r")
print(f.read())
f.close()
with open("new_file2.txt", "r") as f:
    print(f.readlines())


with open("new_file2.txt", "r") as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            break;