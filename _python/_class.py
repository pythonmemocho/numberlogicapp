class Number:
    def __init__(self,num,nums_of_bords) -> None:
        self.number = num
        self.binary_num = str(bin(num)[2:]).zfill(nums_of_bords)
        self.number_group = []
        self.assign_group()

    def assign_group(self):
        for ind, i in enumerate(list(self.binary_num)):
            if i == "1":
                self.number_group.append(ind + 1)


class NumbersBord:
    def __init__(self, value, bord_index) -> None:
        self.bord_index = bord_index
        self._nums = []
        self.id = value

    def insert_nums(self,value):
        self._nums.append(value)