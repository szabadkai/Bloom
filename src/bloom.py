from collections.abc import Sequence


class Bloom:
    def __init__(self, *args):
        self.filter = [False for _ in range(8)]
        self.hash_functions = [lambda x: n * x % 8 for n in range(1, 5)]

        if len(args) == 1 and isinstance(args[0], Sequence):
            for i in args[0]:
                self.add(i)
        else:
            for i in args:
                self.add(i)

    def __eq__(self, other):
        return self.filter == other.filter

    def add(self, item):
        for f in self.hash_functions:
            self.filter[f(item)] = True

    def __contains__(self, item):
        return all((self.filter[f(item)] for f in self.hash_functions))
