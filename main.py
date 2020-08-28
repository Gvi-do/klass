
class Animals:
  meal = 'hungry'
  name = ''
  weight = 0
  all_animals = {}
  heaviest = ''
  total_weight = 0


  def feed(self):
    self.meal = 'not hungry'

  def __init__(self,name,weight):
    self.all_animals[name] = weight
    self.name = name  
    self.weight = weight
    a = 0
    self.heaviest = name
    for k,v in self.all_animals.items():
      if v > a:
        self.heaviest = k
        a = v
    self.total_weight = sum(self.all_animals.values())
class Birds(Animals):
  eggs = 'yes'

  def collect_eggs(self):
    self.eggs = 'no'

class Milk_givers(Animals):
  milk = 'yes'

  def milking(self):
    self.milk = 'no'

class Goose(Birds):
  def __init__(self,name,weight):
    super().__init__(name,weight)
    print(f'Гусь {name}:"Га-га-га"')
    
    
    
class Chicken(Birds):
  def __init__(self,name,weight):
    super().__init__(name,weight)
    print(f'Курица {name}:"Кудах-кудах"') 


class Duck(Birds):
  def __init__(self,name,weight):
    super().__init__(name,weight)
    print(f'Утка {name}:"Кря-кря"') 

class Cow(Milk_givers):
  def __init__(self,name,weight):
    super().__init__(name,weight)
    print(f'Корова {name}:"Муууууууу"')

class Goat(Milk_givers):  
  def __init__(self,name,weight):
    super().__init__(name,weight)
    print(f'Коза {name}:"Бееее"')

class Sheep(Animals):
  wool = 'yes'
  def __init__(self,name,weight):
    super().__init__(name,weight)
    print(f'Овца {name}:"Беееее"(на козу совсем не похоже)')

  def cut(self):
    self.wool = 'bald'


goose1 = Goose('Серый',4)
goose2 = Goose('Белый',5)
goose1.collect_eggs()
goose2.collect_eggs()
print(goose1.eggs)
print(goose2.eggs)
cow_1 = Cow('Манька',80)
cow_1.milking()
print(cow_1.milk)
chicken_1 = Chicken('Ко-ко',2)
chicken_2 = Chicken('Кукареку',3)
chicken_1.collect_eggs()
chicken_2.collect_eggs()
print(chicken_1.eggs)
goat_1 = Goat('Рога',16)
goat_2 = Goat('Копыта',14)
goat_1.milking()
goat_2.milking()
print(goat_1.milk)
sheep1 = Sheep('Барашек',15)
sheep2 = Sheep('Кудрявый',16)
sheep1.cut()
sheep2.cut()
print(sheep1.wool)
duck_1 = Duck('Кряква',4)
duck_1.collect_eggs()
print(duck_1.eggs)

print(f'Самое тяжелое животное - {duck_1.heaviest}')
print(f'Вес всех животных: {duck_1.total_weight}')