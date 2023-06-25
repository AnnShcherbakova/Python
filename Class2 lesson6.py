#Создайте по аналогии два своих файла с любыми классами

class Cat:
    name = None
    age = None
    isHappy = None
    def set_data(self, name, age, isHappy):
        self.name  = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print(self.name, 'age', self.age, '. Happy:', self.isHappy)

cat1 = Cat()
cat1.set_data('Barsik', 3, True)



cat2 = Cat()
cat2.name = 'Daty'
cat2.age = 2
cat2.isHappy = False

cat1.get_data()
print(cat2.name)