from collections import OrderedDict
import math


class Transposition:
    def __init__(self):
        self.key_length = 0
        self.ordered_columns = None
        self.data = str()
        self.number_of_row = 0
        self.cipher = str()
        self.conditions = list()
        self.data_length: int = 0

    def set_key(self, key: str):
        # remove redundant.
        od: OrderedDict = OrderedDict()
        for i in range(len(key)):
            od[key[i]] = i
        filtered_key = list(od.keys())
        self.key_length = len(filtered_key)
        # sort key.
        sorted_key = sorted(filtered_key)
        for i in range(len(filtered_key)):
            od[sorted_key[i]] = i
        # get right order.
        self.ordered_columns = list(range(self.key_length))
        for i in range(self.key_length):
            self.ordered_columns[od[filtered_key[i]]] = i

    def set_filter(self, conditions: list):
        self.conditions = conditions

    def set_plan_text(self, data: str):
        # filter data.
        if len(self.conditions) != 0:
            filtered_data = str()
            for i in data:
                for condition in self.conditions:
                    if condition(i):
                        filtered_data += i
            data = filtered_data
        # complete data.
        self.data_length = len(data)
        self.number_of_row = math.ceil(len(data) / self.key_length)
        padding_length: int = self.number_of_row * self.key_length - len(data)
        self.data = data + ''.join([chr(i) for i in range(ord('a'), ord('a') + padding_length)])

    def encrypt(self):
        self.cipher = str()
        for i in range(self.key_length):
            for j in range(self.number_of_row):
                self.cipher += self.data[self.ordered_columns[i] + j * self.key_length]
        return self.cipher

    def decrypt(self):
        plan = list(range(self.number_of_row * self.key_length))
        for i in range(self.key_length):
            for j in range(self.number_of_row):
                plan[self.ordered_columns[i] + j * self.key_length] = self.cipher[i * self.number_of_row + j]
        return ''.join(plan)
    
    def get_data_length(self):
        return self.data_length


if __name__ == '__main__':
    transposition = Transposition()
    transposition.set_key('securit')
    transposition.set_plan_text('weneedmoresnownow')
    print(transposition.ordered_columns)
    print(transposition.encrypt())
    de = transposition.decrypt()
    print(de)
    print(de[:transposition.get_data_length()])
    pass
