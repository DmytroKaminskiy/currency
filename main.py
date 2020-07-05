class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


c1 = Cat('Tom')
name = str(c1)
print(name)
