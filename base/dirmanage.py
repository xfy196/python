import os
import shutil
print("当前目录:", os.getcwd())
print("当前目录里面有什么:", os.listdir())
os.makedirs("project", exist_ok=True)
print(os.path.exists("project"))


if os.path.exists("user/no"):
    print("user exist")
else:
    os.makedirs("user/no")
    print("user created")
print(os.listdir("user"))
shutil.rmtree("user/no")
print(os.path.basename("new_file.txt"))
def copy(path):
    # 文件名
    filename = os.path.basename(path)
    # 目录名
    dirname = os.path.dirname(path)
    # 新文件名
    new_fielname = "new_" + filename
    # 新路径
    new_path = os.path.join(dirname, new_fielname)
    # 复制
    shutil.copy2(path, new_path)
    return os.path.isfile(new_path), new_path

copy("base/dict.py") 