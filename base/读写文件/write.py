f = open("new_file.txt", "w")
f.write("some.txt...")
f.close()

with open("new_file2.txt", "w") as f:
    f.writelines(["some text for file2...\n", "2nd line\n"])

with open("chinese.txt", "wb") as f:
    f.write("这是中文".encode("utf-8"))