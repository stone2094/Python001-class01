# -*- coding: UTF-8 -*-
'''
具体要求：
定义“动物”、“猫”、“动物园”三个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
'''
from abc import ABCMeta, abstractmethod

class Zoo(object):

    def __init__(self, zoo_name = None):
        print('this is %s zoo' %zoo_name)
        self.animal_list = []

        if zoo_name is None:
            raise Exception("no name for a zoo")
        else :
            self.zoo_name = zoo_name
 
    def add_animal(self,animal = None):
        if hasattr(self, type(animal).__name__) is False:
            setattr(self, type(animal).__name__, [])
        animal_list = getattr(self, type(animal).__name__)
        if animal not in animal_list:
            animal_list.append(animal)
        #animal_list = getattr(self, type(animal).__name__)
        '''
        if animal in self.animal_list:
            print('this animal is existed!')
            
        else:
            self.animal_list.append(animal)
            print('add this animail into the zoo')
            self.__dict__[type(animal).__name__] = animal
        '''   
class Animal(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, species, size, character):
        self.species = species
        self.size = size
        self.character = character

    @property
    def is_fierce(self):
        if self.species == '食肉' and self.character == '凶猛' and self.size != '小':
            return True
        return False

class Cat(Animal):

    voice = 'miao'

    def __init__(self, name, size, like_meat, is_fierce):
        super().__init__(size, like_meat, is_fierce)
        self.name = name
    
    @property
    def is_pet(self):
        return not self.is_fierce

if __name__ == "__main__":
    # 实例化动物园
    z = Zoo('time')
    # 实例化猫cat1
    cat1 = Cat('大花猫1', '食肉', '小型', '温顺')
    # 增加cat1到动物园
    z.add_animal(cat1)
    # 判断动物园是否有猫这种动物
    has_cat = getattr(z, 'Cat')
    print('zoo has cat:{}'.format(bool(has_cat)))
    #print('has_cat:', has_cat)
