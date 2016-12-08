#coding: utf-8

class Material:
    MATERIAL_STONE = 1		# 石头
    MATERIAL_WOOD = 2		# 木材
    MATERIAL_COAL = 3		# 煤炭
    MATERIAL_IRON = 4		# 铁
    def __init__(self, materialType):
        self.materialType = materialType
        self.amount = 0

    # 消耗资源，返回Ture表示资源扣除成功
    def consume(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            return True
        else:
            return False

    # 生成资源
    def produce(self, amount):
        self.amount += amount

    # 返回资源数量
    def getAmount(self):
        return self.amount


    # 获取资源类型
    def getMaterialType(self):
        return self.materialType


class Stone(Material):
    def __init__(self):
        Material.__init__(self, Material.MATERIAL_STONE)

class Wood(Material):
    def __init__(self):
        Material.__init__(self, Material.MATERIAL_WOOD)

class Coal(Material):
    def __init__(self):
        Material.__init__(self, Material.MATERIAL_COAL)

class Iron(Material):
    def __init__(self):
        Material.__init__(self, Material.MATERIAL_IRON)


        
