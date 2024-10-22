class File:
    def __init__(self):
        self.name = "f1"
        self.create_time = "today"
        self.__type = 'txt'
    def change_name(self, new_name):
        self.name = new_name
    def get_info(self):
        print(my_file.__type)
        return self.name + "is created at" + self.create_time

class SonFIle(File):
    def __init__(self):
        super().__init__()

        
my_file = File()
son_file = SonFIle()
my_file.change_name("你好")
print(my_file.get_info())
print(my_file.name)