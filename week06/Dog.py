class Dog(Animal):
    def __init__(self, name, type, size, character):
        super().__init__(self, type, size, character)
        self.name = name

    @property
    def is_pet(self):
        if self.is_beast:
            return False
        else:
            return True
