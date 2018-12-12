from collections import OrderedDict
import math


class Transposition:
    def __init__(self):
        # length of key.
        self.n_col = 0
        self.ordered_columns = None
        self.data = str()
        # number of rows.
        self.n_row = 0
        self.cipher = str()
        self.conditions = list()
        self.data_length: int = 0

    def set_key(self, key: str):
        # remove redundant.
        od: OrderedDict = OrderedDict()
        for i in range(len(key)):
            od[key[i]] = i
        filtered_key = list(od.keys())
        self.n_col = len(filtered_key)
        # sort key.
        sorted_key = sorted(filtered_key)
        for i in range(len(filtered_key)):
            od[sorted_key[i]] = i
        # get right order.
        self.ordered_columns = list(range(self.n_col))
        for i in range(self.n_col):
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
        self.n_row = math.ceil(len(data) / self.n_col)
        padding_length: int = self.n_row * self.n_col - len(data)
        self.data = data + ''.join([chr(i) for i in range(ord('a'), ord('a') + padding_length)])

    def encrypt(self):
        self.cipher = ''.join([self.data[self.ordered_columns[i//self.n_row]+i % self.n_row*self.n_col] for i in range(self.n_col*self.n_row)])
        return self.cipher

    def decrypt(self):
        plan = list(range(self.n_row * self.n_col))
        for i in range(self.n_col):
            for j in range(self.n_row):
                plan[self.ordered_columns[i] + j * self.n_col] = self.cipher[i * self.n_row + j]
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
