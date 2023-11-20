class GeneratorIterator:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self.generator()

    def generator(self):
        for item in self.data:
            yield item

my_list = [1, 2, 3, 4, 5]

iterable = GeneratorIterator(my_list)

for item in iterable:
    print(item)