import random


class Dictogram(dict):
    def __init__(self, iterable=None):
        super(Dictogram, self).__init__()
        self.types = 0
        self.tokens = 0
        if iterable:
            self.update(iterable)

    def update(self, iterable, **kwargs):
        for item in iterable:
            if item in self:
                self[item] += 1
                self.tokens += 1
            else:
                self[item] = 1
                self.types += 1
                self.tokens += 1

    def count(self, item):
        if item in self:
            return self[item]
        return 0

    def return_random_word(self):
        random_key = random.sample(self, 1)
        return random_key[0]

    def return_weighted_random_word(self):
        random_int = random.randint(0, self.tokens - 1)
        index = 0
        list_of_keys = self.keys()
        for i in range(0, self.types):
            index += self[list(list_of_keys)[i]]
            if index > random_int:
                return list(list_of_keys)[i]
