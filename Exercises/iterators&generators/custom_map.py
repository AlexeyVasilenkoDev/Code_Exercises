class CustomMap:
    class CustomMapIter:
        def __init__(self, iterable):
            self.iterable = iterable
            self.pointer = 0

        def __next__(self):
            if self.pointer == len(self.iterable.dict_object.keys()):
                raise StopIteration()
            result = {self.iterable.func1(list(self.iterable.dict_object.items())[self.pointer][0]):
                      self.iterable.func2(list(self.iterable.dict_object.items())[self.pointer][1])}
            self.pointer += 1
            return result

    def __init__(self, dict_object, func1, func2):
        self.dict_object = dict_object
        self.func1 = func1
        self.func2 = func2

    def __iter__(self):
        return self.CustomMapIter(self)


c = CustomMap({'a': 1, 'b': 2, 'c': 53}, lambda x: x.capitalize(), lambda y: y+10)

for i in c:
    print(i)
