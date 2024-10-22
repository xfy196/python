class Calculator:
    def subtract(slef,a ,b):
        return a-b
    def batch_subtract(self, a_list, b_list):
        res_list = []
        for i in range(len(a_list)):
            res_list.append(self.subtract(a_list[i], b_list[i]))

        return res_list

C = Calculator()
print(C.subtract(3,1))
print(C.batch_subtract([3,2,1], [2,3,4]))