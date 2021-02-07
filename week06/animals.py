# 父类
class Animal(object):
    def __init__(self, type, size, character):
        # 定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性
        self.type = type
        self.size = size
        self.character = character

        # ：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
        @property
        def is_ferocious(self):
            if self.type == 'eat_meat' and self.character >= 1 and self.character == 'savage':
                return True
            else:
                return False