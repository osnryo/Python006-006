# 子类
class Cat(Animal):
    # 定义叫声类属性
    sound = '喵'

    def __init__(self, name, type, size, character):
        super().__init__(self, type, size, character)
        self.name = name

    @property
    def is_pet(self):
        if self.is_beast:
            return False
        else:
            return True


