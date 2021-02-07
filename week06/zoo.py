class Zoo(object):
    def __init__(self, name):
        # 普通字段
        self.name = name

    def add_animal(self, name):
        if name not in self.name:
            print('没有同名动物，可添加动物')

