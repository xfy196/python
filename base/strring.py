name = "hello world"
print("%s" % name)
print("{}".format(name))

socre = 1000000
print(f"{socre:,}")
# 删除前后空白
" dad dasd dad ".strip()
print("do tiTle For me".title())

done = False
a = 1 if done else 2
print(a)
d = {"index" + str(i): i*2 for i in range(10)}
print(d)

l = [11,22,33,44]
d = {}
for count, data in enumerate(l, start=5):
    d[count] = data
print(d)
name = ["a", "b", "c"]
score = [1,2,3]
d = {}
for n, s in zip(name, score):
    d[n]=s
print(d)