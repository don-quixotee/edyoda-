class InfIter:
    """Infinite iterator to return all
        even numbers"""

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


i = InfIter()

for n in i:
    if n<20:
        print(n)